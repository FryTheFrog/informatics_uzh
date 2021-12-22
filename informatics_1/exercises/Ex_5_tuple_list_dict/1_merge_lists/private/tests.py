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
    from public.script import merge
except Exception:
    exception = sys.exc_info()[0]


from unittest import TestCase
class PrivateTestSuite(TestCase):

    def _assertType(self, expected, obj):
        if type(obj) != expected:
            m = "@@The return value of your function does not have the right type (list vs. {}).@@".format(type(obj).__name__)
            self.fail(m)

    def _assert(self, a, b, expected, m=None):

        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        # try executing the code
        try:
            actual = merge(a, b)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

        # make sure return type is correct
        self._assertType(list, actual)

        # prepare "default message", if none is provided
        if m == None:
            m = "@@Result is incorrect for a = {}, b = {}.@@".format(a, b)

        # actual unit test
        self.assertEqual(expected, actual, m)


    def test_1(self):
        self._assert([], [], [], "@@Empty lists are not handled correctly.@@")

    def test_2(self):
        self._assert([1], [2], [(1, 2)])

    def test_3(self):
        self._assert([1, 2, 3], [2, 3, 4], [(1, 2), (2, 3), (3, 4)])

    def test_4(self):
        self._assert([1], [], [], "@@The result is not correct if one of both lists is empty.@@")

    def test_5(self):
        self._assert([], [2], [], "@@The result is not correct if one of both lists is empty.@@")

    def test_6(self):
        self._assert([1, 2], [3], [(1, 3), (2, 3)], "@@The result is not correct if both lists do not have the same length.@@")

    def test_7(self):
        self._assert([1], [2, 3], [(1, 2), (1, 3)], "@@The result is not correct if both lists do not have the same length.@@")
