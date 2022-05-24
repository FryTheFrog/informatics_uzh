import ast, os
import inspect
import re
from unittest import TestCase

from public import script

class PrivateTestSuite(TestCase):

    def assert_recursion(self):
        # adopt working directory
        path = "public/script.py" if os.path.exists("public/script.py") else "../public/script.py"
        with open(path) as f:
            tree = ast.parse(f.read())

            v = RecursionTestVisitor()
            v.visit(tree)

            m = "@@Required function 'gcd' not found.@@"
            self.assertTrue("root/gcd" in v.calls.keys(), m)

            m = "@@No recursive call found in the function body of 'gcd'. 'gcd' must call itself.@@"
            self.assertTrue("gcd" in v.calls["root/gcd"], m)

    def _assert(self, a, b, expected, m=None):
        self.assert_recursion()
        actual = script.gcd(a,b)
        m = f"@@gcd({a}, {b}) should be {expected} and not {actual}.@@"
        self.assertEqual(expected, actual, msg=m)

    ## absolute function, basic check of usage
    def test_uses_abs_function(self):
        script_str = inspect.getsource(script)
        num_absolute_value_fcts = " ".join(re.split("#.*\n+", script_str)).count("absolute_value(")
        self.assertGreater(num_absolute_value_fcts, 2, 
        "@@Please use the absolute_value() function in your gcd() function!@@")


    def test_abs_pos(self):
        self.assertEqual(10, script.absolute_value(10),
        f"@@absolute_value({10}) should be {abs(10)} and not {script.absolute_value(10)}.@@")

    def test_abs_neg(self):
        self.assertEqual(10, script.absolute_value(-10), 
        f"@@absolute_value({-10}) should be {abs(10)} and not {script.absolute_value(-10)}.@@")

    ## special cases
    def test_negative_b(self):
        self._assert(30, -1, 1) 

    def test_negative_a(self):
        self._assert(-30, 1, 1) 

    def test_negative_input(self):
        self._assert(-30, -1, 1)

    def test_zero_a(self):
        self._assert(0, 1, 1)

    def test_zero_b(self):
        self._assert(-1, 0, 1)

    def test_zero_input(self):
        self._assert(0, 0, None)

    ## swap
    def test_b_greater_a(self):
        self._assert(16, 24, 8)

    ## normal tests
    def test_a_greater_b(self):
        self._assert(24, 16, 8)

    def test_one(self):
        self._assert(16, 1, 1)

    def test_aprime(self):
        self._assert(33, 16, 1)

    def test_bprime(self):
        self._assert(30, 17, 1)

    def test_2prime(self):
        self._assert(33, 17, 1)

    def test_large_nr(self):
        self._assert(10000000, 2800, 400)



class RecursionTestVisitor(ast.NodeVisitor):

    def __init__(self):
        self.calls = {"root": []}
        self.__scope = ["root"]

    def scopeId(self):
        return "/".join(self.__scope)

    def visit_FunctionDef(self, node):
        self.__scope.append(node.name)
        self.calls[self.scopeId()] = []
        self.generic_visit(node)
        self.__scope.pop()

    def visit_Call(self, node):
        if "id" in node.func._fields:
            self.calls[self.scopeId()].append(node.func.id)
        self.generic_visit(node)
