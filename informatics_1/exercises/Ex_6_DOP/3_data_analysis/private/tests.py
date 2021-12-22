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
    from public.script import gender_class_rates
except Exception:
    exception = sys.exc_info()[0]

# some utility functions
def first(gender):
    return (True, 1, "Some Name", gender, 15.0, 1.23)

def second(gender):
    return (True, 2, "Some Name", gender, 15.0, 1.23)

def third(gender):
    return (True, 3, "Some Name", gender, 15.0, 1.23)

def youngMale(has_survived):
    return (has_survived, 1, "Some Name", "male", 15.0, 1.23)

def oldMale(has_survived):
    return (has_survived, 1, "Some Name", "male", 16.0, 1.23)

def youngFemale(has_survived):
    return (has_survived, 1, "Some Name", "female", 15.0, 1.23)

def oldFemale(has_survived):
    return (has_survived, 1, "Some Name", "female", 16.0, 1.23)

def my_round(survivors, total):
    perc = 100*(survivors/total)
    return round(perc, 1)


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

        # add header and execute
        _in = (
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            _in
        )

        try:
            actual = gender_class_rates(_in)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

        # make sure return type is correct
        self._assertType(tuple, actual, "@@Unexpected return value: The result is not a tuple.@@")
        self.assertEqual(2, len(actual), "@@Unexpected return value: The resulting tuple does not have 2 elements.@@")
        self._assertType(tuple, actual[0], "@@Unexpected return value: The resulting tuple should contain nested tuples.@@")
        self.assertEqual(3, len(actual[0]), "@@Unexpected return value: The nested tuple should have size 3.@@")
        self._assertType(tuple, actual[1], "@@Unexpected return value: The resulting tuple should contain nested tuples.@@")
        self.assertEqual(3, len(actual[1]), "@@Unexpected return value: The nested tuple should have size 3.@@")
        return actual

    def _assert(self, _in, expected, m=None):
        actual = self._exec(_in)

        # prepare "default message", if none is provided
        if not m:
            m = "@@The calculation is not correct for input:\n{}@@".format(_in)

        # actual unit test
        self.assertEqual(expected, actual, m)

    def test0a_check_for_None(self):
        actual = self._exec([first('male')])
#        m1 = actual[0][0] is not None
        m2 = actual[0][1] is not None
        m3 = actual[0][2] is not None
        f1 = actual[1][0] is not None
        f2 = actual[1][1] is not None
        f3 = actual[1][2] is not None
        if m2 or m3 or f1 or f2 or f3:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0b_check_for_None(self):
        actual = self._exec([first('female')])
        m1 = actual[0][0] is not None
        m2 = actual[0][1] is not None
        m3 = actual[0][2] is not None
        # f1 = actual[1][0] is not None
        f2 = actual[1][1] is not None
        f3 = actual[1][2] is not None
        if m1 or m2 or m3 or f2 or f3:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0c_check_for_None(self):
        actual = self._exec([second('male')])
        m1 = actual[0][0] is not None
        # m2 = actual[0][1] is not None
        m3 = actual[0][2] is not None
        f1 = actual[1][0] is not None
        f2 = actual[1][1] is not None
        f3 = actual[1][2] is not None
        if m1 or m3 or f1 or f2 or f3:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0d_check_for_None(self):
        actual = self._exec([second('female')])
        m1 = actual[0][0] is not None
        m2 = actual[0][1] is not None
        m3 = actual[0][2] is not None
        f1 = actual[1][0] is not None
        # f2 = actual[1][1] is not None
        f3 = actual[1][2] is not None
        if m1 or m2 or m3 or f1 or f3:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0e_check_for_None(self):
        actual = self._exec([third('male')])
        m1 = actual[0][0] is not None
        m2 = actual[0][1] is not None
        # m3 = actual[0][2] is not None
        f1 = actual[1][0] is not None
        f2 = actual[1][1] is not None
        f3 = actual[1][2] is not None
        if m1 or m2 or f1 or f2 or f3:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0f_check_for_None(self):
        actual = self._exec([third('female')])
        m1 = actual[0][0] is not None
        m2 = actual[0][1] is not None
        m3 = actual[0][2] is not None
        f1 = actual[1][0] is not None
        f2 = actual[1][1] is not None
        # f3 = actual[1][2] is not None
        if m1 or m2 or m3 or f1 or f2:
            self.fail("@@Parts that do not have any values, should be set to None.@@")


    def test0e_rounded_not_multiplied(self):
        actual = self._exec([first('female'), first('female'), first('male')])
        if type(actual[0][0]) == float and actual[0][0] == 0.3:
            self.fail("@@The implementation does not multiply the results by 100 to get percentages.@@")

    def test0e_not_rounded_not_multiplied(self):
        actual = self._exec([first('female'), first('female'), first('male')])
        if type(actual[0][0]) == float and actual[0][0] > 0.3 and actual[0][0] < 0.34:
            self.fail("@@The implementation does not multiply the results by 100 to get percentages.@@")

    def test0g_not_rounded_multiplied(self):
        actual = self._exec([first('female'), first('female'), first('male')])
        if type(actual[0][0]) == float and actual[0][0] > 33.3 and actual[0][0] < 33.4:
            self.fail("@@The implementation does not round percentages to one decimal digit.@@")

    def test0h_incorrectly_rounded_not_multiplied(self):
        actual = self._exec([first('female'), first('female'), first('male')])
        if actual[0][0] == 0:
            self.fail("@@The implementation is either incorrect or it does not multiply the results by 100 to get percentages.@@")

    def test0i_incorrectly_rounded_multiplied(self):
        actual = self._exec([first('female'), first('female'), first('male')])
        if actual[0][0] == 33:
            self.fail("@@The rounding should preserve one decimal digit, instead, the implementation rounds to an int.@@")

    def test1a_first_male_all(self):
        self._assert([
            first('male')
        ], (
            (100.0, None, None),
            (None, None, None)
        ), "@@The rate of first class male passengers is not correct.@@")

    def test1b_fist_female_all(self):
        self._assert([
            first('female')
        ], (
            (None, None, None),
            (100.0, None, None)
        ), "@@The rate of first class female passengers is not correct.@@")

    def test1c_second_male_all(self):
        self._assert([
            second('male')
        ], (
            (None, 100.0, None),
            (None, None, None)
        ), "@@The rate of second class male passengers is not correct.@@")

    def test1d_second_female_all(self):
        self._assert([
            second('female')
        ], (
            (None, None, None),
            (None, 100.0, None)
        ), "@@The rate of second class female passengers is not correct.@@")

    def test1e_third_male_all(self):
        self._assert([
            third('male')
        ], (
            (None, None, 100.0),
            (None, None, None)
        ), "@@The rate of third class male passengers is not correct.@@")

    def test1f_third_female_all(self):
        self._assert([
            third('female')
        ], (
            (None, None, None),
            (None, None, 100.0)
        ), "@@The rate of third class female passengers is not correct.@@")


    def test2a_first_some(self):
        self._assert([
            first('female'),
            first('female'),
            first('male')
        ], (
            (33.3, None, None),
            (66.7, None, None)
        ), "@@The rates of first class passengers are not correct.@@")

    def test2b_second_some(self):
        self._assert([
            second('female'),
            second('female'),
            second('male')
        ], (
            (None, 33.3, None),
            (None, 66.7, None)
        ), "@@The rates of second class passengers are not correct.@@")

    def test2c_third_some(self):
        self._assert([
            third('female'),
            third('female'),
            third('male')
        ], (
            (None, None, 33.3),
            (None, None, 66.7)
        ), "@@The rates of third class passengers are not correct.@@")

    def test3a_all_male(self):
        self._assert([
            first('male'),
            second('male'),
            third('male')
        ], (
            (33.3, 33.3, 33.3),
            (None, None, None)
        ), "@@The rates of male passengers are not correct.@@")

    def test3a_all_female(self):
        self._assert([
            first('female'),
            second('female'),
            third('female')
        ], (
            (None, None, None),
            (33.3, 33.3, 33.3)
        ), "@@The rates of female passengers are not correct.@@")

    def test5a_integrated_example(self):
        self._assert([
            first('male'),
            first('female'),
            first('female'),
            #
            second('male'),
            second('male'),
            second('female'),
            second('female'),
            #
            third('male'),
            third('male'),
            third('male'),
            third('male'),
            third('female'),
        ], (
            (my_round(1, 12), my_round(2, 12), my_round(4, 12)),
            (my_round(2, 12), my_round(2, 12), my_round(1, 12))
        ), "@@An integrated example that fills all quadrants is not correctly calculated.@@")

    def test5a_integrated_example(self):
        self._assert([
            first('male'),
            first('female'),
            #
            second('male'),
            second('female'),
            second('female'),
            #
            third('male'),
            third('male'),
            third('male'),
            third('male'),
            third('female'),
        ], (
            (my_round(1, 10), my_round(1, 10), my_round(4, 10) ),
            (my_round(1, 10), my_round(2, 10), my_round(1, 10))
        ), "@@An integrated example that fills all quadrants is not correctly calculated.@@")

    def test_rounding_is_correct(self):
        self._assert([
            first('male'),
            first('male'),
            first('male'),
            first('male'),
            first('female'),
            #
            second('male'),
            second('male'),
            second('female'),
            second('female'),
            #

            third('male'),
            third('female'),
        ], (
            (36.4, 18.2, 9.1),
            (9.1, 18.2, 9.1)
        ), "@@The rounding of survival rates is not correct, 66.666... should be rounded to 66.7.@@")