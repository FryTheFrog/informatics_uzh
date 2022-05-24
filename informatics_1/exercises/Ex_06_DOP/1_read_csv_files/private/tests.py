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
    from public.script import read_csv
except Exception:
    exception = sys.exc_info()[0]

# actual test
import os
from unittest import TestCase
from public.script import read_csv

FILE = os.path.dirname(__file__) + "/test.csv"


def delete():
    if os.path.exists(FILE):
        os.remove(FILE)


def write(lines):
    linesWithNewline = [l + "\n" for l in lines]
    with open(FILE, "x") as f:
        f.writelines(linesWithNewline)
    return "\n".join(lines)


class PrivateTestSuite(TestCase):

    def tearDown(self):
        delete()

    # assert that obj has the expected type
    def _assertType(self, expected, obj, m=None):
        if not m:
            m = "@@The return value of the function does not have the right type ({} vs. {}).@@".format(
                expected.__name__, type(obj).__name__)
        if type(obj) != expected:
            self.fail(m)

    # try executing the code, fails gracefully
    def _exec(self):
        try:
            return read_csv(FILE)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

    def _assert(self, _in, expected, m=None):
        # make sure file does not exist
        delete()

        # abort execution, when import did not work
        if exception:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        content = write(_in)
        actual = self._exec()

        self._assertType(list, actual)
        if len(actual):
            self._assertType(tuple, actual[0], "@@Values in the returned list should be tuples, but they are {}.@@".format(type(actual[0]).__name__))
            if len(actual[0]):
                self._assertType(str, actual[0][0], "@@Values in the returned list should be strings, but they are {}.@@".format(
                    type(actual[0][0]).__name__))

        if not m:
            m = "@@The implementation cannot parse the following file contents correctly:\n{}@@".format(content)
        self.assertEqual(expected, actual, m)

    def test1_empty_file(self):
        self._assert([], [], "@@The implementation does not handle empty files correctly.@@")

    def test2_hint_forgot_to_remove_nl(self):
        write(["a"])
        actual = read_csv(FILE)
        if actual == [("a\n",)]:
            self.fail("@@The implementation does not remove the newline characters '\\n' from the end of the line.@@")

    def test3_one_line_one_attrib(self):
        m = "@@The implementation does not handle .csv files with one record and one attribute correctly.@@"
        self._assert(["a"],[("a",)], m)

    def test4_one_line_two_attrib(self):
        m = "@@The implementation does not handle .csv files with one record and two attributes correctly.@@"
        self._assert(["a,b"],[("a", "b")], m)

    def test5_one_line_no_type_conversion(self):
        m = "@@The implementation does not store all attributes as string values.@@"
        self._assert(["a,1,2.34"],[("a", "1", "2.34")], m)

    def test6_two_lines_one_attribute(self):
        m = "@@The implementation does not handle .csv files with two records and one attribute correctly.@@"
        self._assert(["a", "b"],[("a",), ("b",)], m)

    def test6_two_lines_two_attributes(self):
        m = "@@The implementation does not handle .csv files with two records and two attributes correctly.@@"
        self._assert(["a,b", "c,d"],[("a","b"), ("c","d")], m)

    def test7_empty_line(self):
        # It is bad testing practice to have multiple asserts in one test, this method should have
        # been split into three tests. However, this would have added a lot of importance to this
        # check, which we wanted to avoid for the grading.
        m = "@@The implementation does not ignore empty lines at the start of a .csv file.@@"
        self._assert(["", "b"],[("b",)], m)
        m = "@@The implementation does not ignore empty lines in the middle of a .csv file.@@"
        self._assert(["a", "", "c"],[("a",), ("c",)], m)
        m = "@@The implementation does not ignore empty lines at the end of a .csv file.@@"
        self._assert(["a", ""],[("a",)], m)

    def test8_basic_case_empty_attribute(self):
        write(["a,,c"])
        actual = read_csv(FILE)
        expected = [("a","","c")]
        m = "@@The implementation does not handle empty attributes correctly.@@"
        self.assertEqual(expected, actual, m)
