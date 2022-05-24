#!/usr/bin/env python3

# replace input implementation
import builtins, sys
class YouCannotUseInputInACCESSException(Exception): pass
def crashing_input(prompt):
    raise YouCannotUseInputInACCESSException("You cannot use 'input' in the grading environment.")
builtins.input_orig = builtins.input
builtins.input = crashing_input

# catch potential exception from import
exception = None
try:
    from public.script import visualize
except Exception:
    exception = sys.exc_info()[0]

# some utility functions
def alive(t_class):
    return (True, t_class, "Some Name", "male", 18, 1.23)

def dead(t_class):
    return (False, t_class, "Some Name", "male", 18, 1.23)

def allAlive():
    return [
        alive(1),
        alive(2),
        alive(3),
    ]

def expectation(data):
    expect = []
    total = data[0][1] + data[1][1] + data[2][1]
    for idx, title in enumerate(["1st Class", "2nd Class", "3rd Class"]):
        expect.append("== {} ==".format(title))
        expect.append(bar("Total", data[idx][1], total))
        expect.append(bar("Alive", data[idx][0], data[idx][1]))
    return "\n".join(expect)

def bar(title, a, b):
    perc = round(100*a/b, 1)
    num_symbol = round(perc/5)
    num_space = 20 - num_symbol
    return "{} |{}{}| {}%".format(title, num_symbol*"*", num_space*" ", perc)


from unittest import TestCase
class PrivateTestSuite(TestCase):

    # assert that obj has the expected type
    def _assertType(self, expected, obj, m=None):
        if type(obj) != expected:
            if not m:
                m = "@@The return value of your function does not have the right type ({} vs. {}).@@".format(expected.__name__, type(obj).__name__)
            self.fail(m)

    # try executing the code, fails gracefully
    def _exec(self, _in):
        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        try:
            _in = (
                ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
                _in
            )
            out = visualize(_in)

            # make sure return type is correct
            self._assertType(str, out)
            out = out.strip()  # trailing newlines
            out = out.replace("\r\n", "\n")  # windows newlines
            out = out.replace(",", ".")  # german number formatting
            return out
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

    def _execAndParse(self, _in):
        # add header and execute
        actual = self._exec(_in)
        actual = actual.split("\n")
        return actual

    def _assert(self, _in, expected, m=None):
        # add header and execute
        actual = self._exec(_in)

        # prepare "default message", if none is provided
        if not m:
            m = "@@The calculation is not correct for input:\n{}@@".format(_in)

        # actual unit test
        self.assertEqual(expected, actual)

    def test0a_should_be_9_lines(self):
        actual = self._execAndParse(allAlive())
        m = "@@The output does not have the expected 9 lines.@@"
        self.assertEqual(9, len(actual), m)


    def test0b_should_contain_certain_symbols(self):
        actual = "\n".join(self._execAndParse(allAlive()))
        symbols = "=|%*. \n"
        for char in symbols:
            m = "@@Surprisingly, the character '{}' is not used in the output.@@".format(char)
            self.assertTrue(char in actual)
        for char in actual:
            if char.isdigit() or char.isalnum() or char in symbols:
                continue
            m = "@The solution contain the character '{}', which breaks with the defined schema.@".format(char)
            self.fail(m)

    def test0c_should_have_uppercase_titles(self):
        actual = "\n".join(self._execAndParse(allAlive()))
        for lc_word in ["class", "total", "alive"]:
            if lc_word in actual:
                m = "@@The output is not correct. It contain the lower-case '{}', while the first letter should be upper-case.@@".format(lc_word)
                self.fail(m)

    def test0d_should_have_three_titles(self):
        actual = self._execAndParse(allAlive())
        m = "@@Line {} does not equal the expected '{}'.@@"
        for lineNum, title in [(0, "== 1st Class =="),(3, "== 2nd Class =="),(6, "== 3rd Class ==")]:
            if actual[lineNum] != title:
                self.fail(m.format(lineNum, title))

    def test0e_should_have_formatting_spaces_start(self):
        actual = self._execAndParse(allAlive())
        m = "@@Line {} does not start with the expected '{}'.@@"
        for lineNum, title in [(1, "Total |"),(2, "Alive |"),(4, "Total |"),(5, "Alive |"),(7, "Total |"),(8, "Alive |")]:
            if not actual[lineNum].startswith(title):
                self.fail(m.format(lineNum, title))

    def test0f_should_have_percentage_sign(self):
        actual = self._execAndParse(allAlive())
        for lineNum in [1, 2, 4, 5, 7, 8]:
            if not actual[lineNum].endswith("%"):
                m = "@@Line {} should end with the % sign.@@"
                self.fail(m.format(lineNum))

    def test0g_should_have_0_100_numbers(self):
        actual = self._execAndParse([
            alive(1),
            dead(1),
            dead(2),
            alive(3)
        ])
        if actual[1].endswith(" 0.5%"):
            m = "@@The percentage numbers should be multiplied by 100, so they are in the range [0, 100].@@"

    def test0h_should_have_formatting_spaces_end(self):
        actual = self._execAndParse([
            alive(1),
            dead(1),
            dead(2),
            alive(3)
        ])
        for lineNum, title in [(1, "| 50.0%"),(2, "| 50.0%")]:
            if not actual[lineNum].endswith(title):
                m = "@@Either the calculation for Total/Alive percentages is not correct, or the formatting does not include a space between '|' and the number.@@"
                self.fail(m.format(lineNum, title))
        if not actual[5].endswith("| 0.0%"):
            m = "@@The decimal point does not need to be aligned. For 0%, the lines should end with '| 0.0%'.@@"
            self.fail(m)
        if not actual[8].endswith("| 100.0%"):
            m = "@@The decimal point does not need to be aligned. For 100%, the lines should end with '| 100.0%'.@@"
            self.fail(m)

    def test0i_should_not_have_empty_lines(self):
        actual = self._execAndParse([
            alive(1),
            dead(1),
            dead(2),
            alive(3)
        ])
        if "" in actual:
            self.fail("@@The output should not contain empty lines.@@")

    def test0j_check_for_zero_stars(self):
        actual = self._execAndParse([
            alive(1),
            dead(1),
            dead(2),
            alive(3)
        ])
        if "*" in actual[5]:
            m = "@@For 0%, the bar should not contain any '*'.@@"
            self.fail(m)
        if "|  " in actual[8] or "  |" in actual[8]:
            m = "@@For 100%, the bar should be completely filled with '*'.@@"
            self.fail(m)

    def test0j_length_of_bars(self):
        actual = self._execAndParse([
            alive(1),
            dead(1),
            dead(2),
            alive(3)
        ])
        for l in actual:
            if "|" in l:
                idx_first_content = l.find("|") + 1
                idx_last_content = l.find("|", idx_first_content)
                bar_width = idx_last_content - idx_first_content
                m="@@The bar width is not correct. It should be 20, but it is {}.@@".format(bar_width)
                self.assertEqual(20, bar_width, m)

    def test0k_check_for_rounding_up_stars(self):
        actual = self._execAndParse([
            alive(1),
            alive(1),
            alive(1),
            alive(2),
            alive(2),
            alive(2),
            alive(3)
        ])
        if not "|*********           |" in actual[1]:
            m = "@@Rounding the number of stars does not work correctly. For 42.9%, nine * should be drawn.@@"
            self.fail(m)

    def test0l_check_for_rounding_down_stars(self):
        actual = self._execAndParse([
            alive(1),
            alive(2),
            alive(3),
            alive(3),
            alive(3),
            alive(3),
        ])
        if not "|***                 |" in actual[1]:
            m = "@@Rounding the number of stars does not work correctly. For 16.7%, three '*' should be drawn.@@"
            self.fail(m)

    def test1_all_survive(self):
        self._assert([
            alive(1),
            alive(2),
            alive(3),
        ], expectation(((1, 1),(1, 1),(1, 1))),
        "@@Visualization is not correct if all survive.@@")

    def test2_no_survivors(self):
        self._assert([
            dead(1),
            dead(2),
            dead(3),
        ], expectation(((0, 1),(0, 1),(0, 1))),
        "@@Visualization is not correct if all die.@@")

    def test3_mixed(self):
        self._assert([
            alive(1),
            dead(1),
            #
            alive(2),
            dead(2),
            dead(2),
            #
            alive(3),
            dead(3),
            dead(3),
            dead(3),
        ], expectation(((1, 2), (1, 3), (1, 4))))
