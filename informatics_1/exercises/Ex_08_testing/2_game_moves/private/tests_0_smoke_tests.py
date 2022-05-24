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
    from public.script import move
except Exception:
    exception = sys.exc_info()[0]


from unittest import TestCase
class PrivateTestSuite(TestCase):

    # assert that obj has the expected type
    def _assertType(self, expected, obj, m):
        if type(obj) != expected:
            self.fail(m)

    def test_provided_example(self):

        if exception:
            m = "@@Failed to import the solution for running the test that has been provided in the template ({}). " \
                "Make sure that a Test&Run works before attempting any submission.@@".format(exception.__name__)
            self.fail(m)

        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )

        try:
            actual = move(state, "right")
        except:
            e_type = sys.exc_info()[0]
            m = "@@Running the test that has been provided in the template failed with an error ({}). " \
                "Make sure that a Test&Run works before attempting any submission.@@".format(e_type.__name__)
            self.fail(m)

        self._assertType(tuple, actual, "@@Incorrect return type when running the test from the template, "
                                        "tuple expected.@@")
        self._assertType(tuple, actual[0], "@@First element of returned tuple is not a tuple when running "
                                           "the test from the template.@@")
        if actual[0]:
            self._assertType(str, actual[0][0], "@@First element of returned tuple should be a tuple and "
                                                "contain strings when running the test from the template.@@")
        else:
            self.fail("@@Running the test from the template failed. The first element of the returned tuple "
                      "should be a non-empty tuple.@@")
        self._assertType(tuple, actual[1], "@@Second element of returned tuple is not a tuple when running "
                                           "the test from the template.@@")
        if actual[1]:
            self._assertType(str, actual[1][0], "@@Second element of returned tuple should be a tuple and "
                                                "contain strings when running the test from the template.@@")
        else:
            self.fail("@@Running the test from the template failed. The second element of the returned "
                      "tuple should be a non-empty tuple.@@")

        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual, "@@The result is not correct when running the test that has been "
                                           "provided in the template. Please test your implementation thorughly "
                                           "before attempting any submission.@@")
