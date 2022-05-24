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
    from public.script import preprocess
except Exception:
    exception = sys.exc_info()[0]

HEADER_TUPLE = ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare')

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
        try:
            return preprocess(_in)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

    def _assert(self, _in, expectedTuples, m=None):

        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        # prepend header
        _in = [HEADER_TUPLE] + _in
        expected = (
            HEADER_TUPLE,
            expectedTuples
        )
        actual = self._exec(_in)

        # make sure return type is correct
        self._assertType(tuple, actual, "@@The implementation does not follow the specification. The return value should be a tuple.@@")
        self.assertEqual(2, len(actual), "@@The implementation does not follow the specification. The return value should be a tuple of size 2.@@")
        self._assertType(tuple, actual[0], "@@The implementation does not follow the specification. The first value in the returned tuple should be a tuple with the headers.@@")
        self._assertType(list, actual[1], "@@The implementation does not follow the specification. The second value in the returned tuple should be the list of all value.@@")
        if len(actual[1]):
            self._assertType(tuple, actual[1][0], "@@The implementation does not follow the specification. The second value in the returned tuple should be the list of all values. All these records should be tuples.@@")

        # prepare "default message", if none is provided
        if not m:
            m = "@@The implementation created an unexpected result for:\n{}@@".format(_in)

        self.assertEqual(expected, actual, m)

    def test0_no_record(self):
        self._assert([], [], "@@The implementation cannot handle cases that only consist of the header without any further records.@@")

    def test0_failing_casts(self):
        # stop if the implementation does not even work for basic cases
        try: preprocess([('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'), ('yes', '1', 'Some Name', 'male', '12', '1')])
        except: return

        missing_cases = [
            ('yes', '', 'Some Name', 'male', '12', '1'),
            ('yes', '1', 'Some Name', 'male', '', '1'),
            ('yes', '1', 'Some Name', 'male', '12', ''),
        ]
        for c in missing_cases:
            try: preprocess([('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'), c,])
            except:
                self.fail("@@The number fields (i.e., ticket class, age, or fare) might be empty. This must be checked or a conversion will fail.@@")

        float_cases = [
            ('yes', '1', 'Some Name', 'male', '12.34', '1'),
            ('yes', '1', 'Some Name', 'male', '12', '1.23'),
        ]
        for c in float_cases:
            try: preprocess([('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'), c,])
            except:
                self.fail("@@Some of the number fields are floats (i.e., age or fare), a cast to int does not work in all cases.@@")

    def test1_single_exemplary_record(self):
        _in = [('no', '3', 'Some Name', 'male', '22', '7.25')]
        self._assert(_in,
                     [(False, 3, 'Some Name', 'male', 22.0, 7.25),],
                     "@@The implementation cannot handle standard cases like {}.@@".format(_in))

    def test2_another_exemplary_record(self):
        _in = [('yes', '2', 'Other Name', 'female', '18', '12.34')]
        self._assert(_in,
                     [(True, 2, 'Other Name', 'female', 18.0, 12.34),],
                     "@@The implementation cannot handle standard cases like {}.@@".format(_in))

    def test3a_survived_yes(self):
        self._assert([('True', '3', 'Some Name', 'male', '22', '7.25')],
                     [(True, 3, 'Some Name', 'male', 22.0, 7.25),],
                     "@@Normalization does not work, if the 'Survived' attribute is set to 'True'.""@@")

    def test3b_survived_no(self):
        self._assert([('False', '3', 'Some Name', 'male', '22', '7.25')],
                     [(False, 3, 'Some Name', 'male', 22.0, 7.25),],
                     "@@Normalization does not work, if the 'Survived' attribute is set to 'False'.""@@")

    def test3c_survived_missing(self):
        self._assert([('', '3', 'Some Name', 'male', '22', '7.25')],
                     [],
                     "@@Cases with missing 'Survived' attribute do not get filtered.""@@")

    def test3d_survived_cannot_be_parsed(self):
        self._assert([('undefined', '3', 'Some Name', 'male', '22', '7.25')],
                     [],
                     "@@Cases with undefined 'Survived' attribute do not get filtered (e.g., 'unknown').""@@")

    def test3e_survived_normalized(self):
        pos_cases = ['Alive', 'Survived', 'T', 'True', 'Yes', 'survived', 't', 'true', 'yes']
        neg_cases = ['Dead', 'F', 'False', 'No', 'Survived=dead', 'dead', 'f', 'false', 'no']

        for case in pos_cases:
            self._assert([(case, '3', 'Some Name', 'male', '22', '7.25')],
                         [(True, 3, 'Some Name', 'male', 22.0, 7.25),],
                         "@@The normalization of the 'Survived' attribute does not consider the case '{}'.@@".format(case))
        for case in neg_cases:
            self._assert([(case, '3', 'Some Name', 'male', '22', '7.25')],
                         [(False, 3, 'Some Name', 'male', 22.0, 7.25),],
                         "@@The normalization of the 'Survived' attribute does not consider the case '{}'.@@".format(case))

    def test4a_ticket_class_all_valid(self):
        for t_class in [1, 2, 3]:
            self._assert([('no', str(t_class), 'Some Name', 'male', '22', '7.25')],
                         [(False, t_class, 'Some Name', 'male', 22.0, 7.25),],
                         "@@The normalization does not work for valid ticket classes like '{}'.@@".format(t_class))

    def test4b_ticket_class_invalid(self):
        self._assert([('no', "0", 'Some Name', 'male', '22', '7.25')],
                     [],
                     "@@Invalid ticket classes like '0' do not get filtered.@@")
        self._assert([('no', "4", 'Some Name', 'male', '22', '7.25')],
                     [],
                     "@@Invalid ticket classes like '4' do not get filtered.@@")

    def test4b_ticket_class_missing(self):
        self._assert([('no', "", 'Some Name', 'male', '22', '7.25')],
                     [],
                     "@@The normalization does not filter records when the ticket class is missing.@@")

    def test5_name_mising(self):
        self._assert([('no', "1", '', 'male', '22', '7.25')],
                     [],
                     "@@The normalization does not filter records when the name is missing.@@")

    def test6a_gender_male(self):
        self._assert([('no', "1", 'Some Name', 'male', '22', '7.25')],
                     [(False, 1, 'Some Name', 'male', 22.0, 7.25),],
                     "@@The normalization does not recognize 'male' as a valid gender.@@")

    def test6b_gender_female(self):
        self._assert([('no', "1", 'Some Name', 'female', '22', '7.25')],
                     [(False, 1, 'Some Name', 'female', 22.0, 7.25),],
                     "@@The normalization does not recognize 'female' as a valid gender.@@")

    def test6c_gender_missing(self):
        self._assert([('no', "1", 'Some Name', '', '22', '7.25')],
                     [],
                     "@@The normalization does not filter records when the gender is missing.@@")

    def test6d_gender_cannot_be_parsed(self):
        self._assert([('no', "1", 'Some Name', 'undefined', '22', '7.25')],
                     [],
                     "@@The normalization does not filter records when the gender cannot be determined (e.g., 'Unknown').@@")

    def test6e_gender_normalization(self):
        male = ['male', 'Male', 'm', 'M']
        female = ['female', 'Female', 'f', 'F']

        for gender in male:
            self._assert([('no', "1", 'Some Name', gender, '22', '7.25')],
                         [(False, 1, 'Some Name', 'male', 22.0, 7.25),],
                         "@@The normalization does not recognize '{}' as 'male'.@@".format(gender))
        for gender in female:
            self._assert([('no', "1", 'Some Name', gender, '22', '7.25')],
                         [(False, 1, 'Some Name', 'female', 22.0, 7.25),],
                         "@@The normalization does not recognize '{}' as 'female'.@@".format(gender))

    def test7a_age(self):
        self._assert([('no', "1", 'Some Name', 'male', '22', '7.25')],
                     [(False, 1, 'Some Name', 'male', 22.0, 7.25),],
                     "@@The normalization does not recognize '22' as a valid age.@@")

    def test7b_age_invalid(self):
        self._assert([('no', "1", 'Some Name', 'male', '0', '7.25')],
                     [],
                     "@@The normalization does not recognize '0' as an invalid age.@@")
        self._assert([('no', "1", 'Some Name', 'male', '101', '7.25')],
                     [],
                     "@@The normalization does not recognize '101' as an invalid age.@@")

    def test7c_age_missing(self):
        self._assert([('no', "1", 'Some Name', 'male', '', '7.25')],
                     [],
                     "@@The normalization does not filter records when the age is missing.@@")

    def test8a_fare(self):
        self._assert([('no', '3', 'Some Name', 'male', '22', '7.25')],
                     [(False, 3, 'Some Name', 'male', 22.0, 7.25),],
                     "@@The normalization does not recognize '7.25' as a valid fare.@@")

    def test8a_fare_missing(self):
        self._assert([('no', '3', 'Some Name', 'male', '22', '')],
                     [(False, 3, 'Some Name', 'male', 22.0, 25.0),],
                     "@@The normalization does not set the default fare, when the fare is missing.@@")

    def test8a_fare_too_small(self):
        self._assert([('no', '3', 'Some Name', 'male', '22', '-17')],
                     [(False, 3, 'Some Name', 'male', 22.0, 25.0),],
                     "@@The normalization does not fix cases, in which the fare is negative.@@")
