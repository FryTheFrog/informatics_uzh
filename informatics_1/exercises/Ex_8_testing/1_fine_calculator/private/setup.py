#!/usr/bin/env python3
import os, subprocess, sys, ast
from shutil import rmtree
from shutil import copyfile

CWD = os.getcwd()
print("File: {}".format(__file__))
print("CWD:  {}".format(CWD))
TESTS_SRC = "public/tests.py"
TESTS_DEST = "tmp/" + TESTS_SRC
TESTS_GEN = "tmp/"
DIR_CORRECT = "private/correct"
DIR_INCORRECT = "private/incorrect"
PREFIX_HINT = "# Hint:"

assert (os.path.isdir("public"))
assert (os.path.isfile(TESTS_SRC))
assert (os.path.isdir("private"))
assert (os.path.isdir(DIR_CORRECT))
assert (os.path.isdir(DIR_INCORRECT))


def run():

    print("Searching for solutions...")

    print("\t{}...".format(DIR_CORRECT))
    pos = find_solutions(DIR_CORRECT, True)

    print("\t{}...".format(DIR_INCORRECT))
    neg = find_solutions(DIR_INCORRECT, False)

    print("Found solutions:")
    for s in pos + neg:
        print("- " + str(s))

    if len(pos) != len(neg):
        sys.stdout.write("Imbalanced number of cases ({}x pos, {}xneg), resampling ".format(len(pos), len(neg)))
        if len(pos) < len(neg):
            print("positive cases:")
            pos = resample(pos, len(neg))
        else:
            print("negative cases:")
            neg = resample(neg, len(pos))

        print("After resampling:")
        for s in pos + neg:
            print("- " + str(s))

    err = submission_has_tests()
    if err == None:
        res = exe(pos + neg)
    else:
        res = [EvalResult(None, False, False, err)] * 2*len(pos)

    os.chdir(CWD)
    gen_results(res)


def resample(slns, count):
    res = []
    idx = 0
    while len(res) < count:
        res.append(slns[idx])
        idx = (idx + 1) % len(slns)
    return res

def gen_results(res):
    lines = [
        "from unittest import TestCase",
        "class GeneratedTestSuite(TestCase):"
    ]


    test_num = 0 # required for resampled cases, which create duplicate test names!
    for eval_result in res:
        test_num += 1

        if eval_result.error is not None:
            lines.append("\tdef test{}_failure(self):".format(test_num))
            lines.append("\t\tself.fail(\"@@{}@@\")".format(eval_result.error))
            continue

        sln = eval_result.sln

        lines.append("\tdef test{}_{}(self):".format(test_num, sln.get_name()))

        if eval_result.has_crashed:
            m = eval_result.error if eval_result.error else sln.hint
            lines.append("\t\tself.fail(\"@@Execution crashed: {}@@\")".format(m))
            continue

        if sln.should_pass == eval_result.has_ended_successfully:
            state = "Worked" if sln.should_pass else "Failed"
            lines.append("\t\t\"{}, as expected: {}\"".format(state, sln.hint))
            continue

        if sln.should_pass:
            m = "A correct solution did not pass your test suite: {}".format(sln.hint)
        else:
            m = "Your test suite did not detect an issue in a hidden implementation: {}".format(sln.hint)
        lines.append("\t\tself.fail(\"@@{}@@\")".format(m))

    lines.append("")
    content = "\n".join(lines)

    with open("private/tests_generated.py", "w") as g:
        g.write(content)


def exe(solutions):
    res = []
    for sln in solutions:
        print("-------------")
        print("Executing {}...".format(sln))

        os.chdir(CWD)
        if os.path.exists("tmp"):
            rmtree("tmp")
        os.makedirs("tmp/public")

        copyfile(TESTS_SRC, TESTS_DEST)
        print("Copying {} to {}...".format(TESTS_SRC, TESTS_DEST))
        SCRIPT_DEST = "tmp/public/script.py"
        print("Copying {} to {}...".format(sln.path, SCRIPT_DEST))
        copyfile(sln.path, SCRIPT_DEST)

        os.chdir("tmp")
        print("now in: " + os.getcwd())

        #cmd = "/usr/bin/python --version"
        cmd = "python -m unittest public/tests.py"
        print("executing '{}'...".format(cmd))
        out = subprocess.Popen(cmd,
                               cwd=os.getcwd(),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

        stdout, stderr = out.communicate()

        if stdout:
            stdout = stdout.decode("UTF-8")
        if stderr:
            stderr = stderr.decode("UTF-8")

        last_line = stdout.split("\n")[-2]
        has_crashed = not (last_line == "OK" or last_line.startswith("FAILED")) # fail vs. error
        has_ended_successfully = not out.returncode

        # handle cases, in which the execution crashed unexpectedly
        error = parse_error(stdout)
        if sln.should_pass and error:
            if error == "AssertionError":
                m = "Your test suite contains a test that fails for a correct implementation ({}).".format(sln.hint)
            elif error == "UserWarning":
                uw_hint = None
                for l in stdout.split("\n"):
                    if l.startswith("UserWarning"):
                        idx1 = l.find("@@")
                        if idx1 != -1:
                            idx2 = l.find("@@", idx1+2)
                            if idx2 != -1:
                                uw_hint = l[idx1+2:idx2]
                if uw_hint:
                    m = "Your test suite failed for a correct implementation. Hint: {}".format(uw_hint)
                else:
                    m = "Your test suite failed for a correct implementation: {}".format(sln.hint)
            else:
                m = "Running your test suite on a correct implementation failed due to a '{}'.".format(error)
            res.append(EvalResult(sln, True, False, m))
        else:
            res.append(EvalResult(sln, has_crashed, has_ended_successfully))

    os.chdir(CWD)
    if os.path.exists("tmp"):
        rmtree("tmp")
    return sorted(res)


def parse_error(stdout):
    if "Traceback" in stdout:
        lines = stdout.split("\n")
        lines = [l for l in lines if l] # filter empty lines
        idx_trace = 0
        for l in lines: # find segment that contains crash
            if l.startswith("Traceback"):
                break
            idx_trace += 1
        if idx_trace < len(lines):
            lines = lines[idx_trace:]
            idx_splitter = 0
            for l in lines: # find end of segment
                if l.startswith("-----"):
                    break
                idx_splitter += 1
            error = "unknown"
            for l in lines[idx_splitter-1:0:-1]: # travel back up to find error line
                if len(l) > 0 and l[0].isalpha() and not ( # skip lines that don't start with alpha
                  l.startswith("FAIL:") or l.startswith("OK:")): # skip own error reporting
                    error = l
                    break
            if ":" in error:
                if error.startswith("AssertionError"):
                    return error
                error = error[:error.find(":")]
                if "Error" in error or "Exception" in error or "UserWarning" in error:
                    return error
        return "Unknown Error"
    return None


def find_solutions(base, should_pass):
    solutions = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.endswith(".py") and not f == "__init__.py":
                with open(root + "/" + f, "r") as f2:
                    hint = f2.readlines()[1]
                    if len(hint) < len(PREFIX_HINT) or not hint.startswith(PREFIX_HINT):
                        raise Exception(
                            "Error in solution file '{}': (In-) Correct Solutions must start with a solution hint!".format(
                                f))
                    hint = hint[len(PREFIX_HINT):].strip()
                    s = Solution(root +"/" + f, hint, should_pass)
                    print("\t\t" + str(s))
                    solutions.append(s)
    return solutions


class Solution:
    def __init__(self, path, hint, should_pass):
        self.path = path
        self.hint = hint
        self.should_pass = should_pass
        self.should_fail = not should_pass

    def __gt__(self, other):
        if isinstance(other, Solution):
            return self.path > other.path
        else:
            return -1

    def get_name(self):
        return os.path.basename(self.path)[:-3]

    def __str__(self):
        return "Solution({}, pass:{}, hint:'{}')".format(self.path, "OK" if self.should_pass else "FAIL", self.hint)


class EvalResult:
    def __init__(self, sln, has_crashed, has_ended_successfully, error=None):
        self.sln = sln
        self.has_crashed = has_crashed
        self.has_ended_successfully = has_ended_successfully
        self.error = error

    def __gt__(self, other):
        if isinstance(other, EvalResult):
            return self.sln > other.sln
        else:
            return -1

    def __str__(self):
        return "EvalResult({}, crash:{}, success:{})".format(self.sln, self.has_crashed, self.has_ended_successfully)


def submission_has_tests():
    try:
        with open(TESTS_SRC) as f:
            tree = ast.parse(f.read())
            #print(ast.dump(tree))

            v = TestIdentificationVisitor()
            v.visit(tree)

            #print ("#tests: {}".format(v.num_tests))
            #print ("#asserts: {}".format(v.num_asserts))

            if v.error:
                return v.error
            elif not v.has_test_class:
                return "Could not find a test suite that inherits from TestCase."
            elif v.num_tests == 0:
                    return "The test suite did not define any tests."
            elif v.num_asserts == 0:
                return "No assertions like self.assertEqual or self.fail found in any of the tests."
        return None
    except Exception as e:
        return "The test suite cannot be parsed due to a '{}'.".format(type(e).__name__)


class TestIdentificationVisitor(ast.NodeVisitor):

    def __init__(self):
        self.test_names = []
        self.in_test_class = False
        self.in_test_fun = False
        self.has_test_class = 0
        self.num_tests = 0
        self.num_asserts = 0
        self.error = None

    def visit_ClassDef(self, node):
        bases = [n.id for n in node.bases]
        if "TestCase" in bases:
            self.has_test_class = True
            self.in_test_class = True
            self.generic_visit(node)
            self.in_test_class = False

    def visit_FunctionDef(self, node):
        if self.in_test_class:
            if node.name.startswith("test"):
                if node.name in self.test_names:
                    self.error = "Multiple definitions of '{}' exist in your test suite, which shadow each other.".format(node.name)
                self.test_names.append(node.name)

                self.num_tests += 1
                self.in_test_fun = True
                self.generic_visit(node)
                self.in_test_fun = False

    def visit_Call(self, node):
        if self.in_test_fun:
            if hasattr(node.func, "attr"):
                if node.func.attr.startswith("assert") or node.func.attr.startswith("fail"):
                    self.num_asserts += 1


run()
