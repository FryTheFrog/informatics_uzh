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
    from public.script import analyze
except Exception:
    exception = sys.exc_info()[0]


from unittest import TestCase
class PrivateTestSuite(TestCase):

    # assert that obj has the expected type
    def _assertType(self, expected, obj):
        if type(obj) != expected:
            m = "@@The return value of your function does not have the right type ({} vs. {}).@@".format(expected.__name__, type(obj).__name__)
            self.fail(m)

    # try executing the code, fails gracefully
    def _exec(self, _in):
        try:
            return analyze(_in)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

    def _assert(self, _in, expected, m=None):

        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        actual = self._exec(_in)

        # make sure return type is correct
        self._assertType(dict, actual)

        # prepare "default message", if none is provided
        if m == None:
            if len(_in) == 1:
                m = "@@Hashtag extraction is not correct for '{}'.@@".format(_in[0])
            else:
                m = "@@Result is incorrect for the following list of posts: {}@@".format(_in)

        # actual unit test
        self.assertEqual(expected, actual, m)



    def test01_empty_list(self):
        self._assert([], {}, "@@The result is not correct for an empty list of posts.@@")

    def test02_empty_string(self):
        self._assert([""], {}, "@@The result is not correct for an empty posts.@@")

    def test03_no_hashtag_removal(self):
        actual = self._exec(["text #a text"])
        if "#a" in actual.keys():
            self.fail("@@The implementation does not remove the '#' symbol from the hashtags.@@")

    def test04_ht_detection_1(self):
        self._assert(["text #b text"], {"b": 1})

    def test05_ht_detection_end(self):
        self._assert(["text #a"], {"a": 1}, "@@The implementation does not recognize hashtags at the end of the sentence.@@")

    def test06_ht_detection_start(self):
        self._assert(["#a text"], {"a": 1}, "@@The implementation does not recognize hashtags at the beginning of the sentence.@@")

    def test07_empty_hashtag(self):
        self._assert(["#"], {}, "@@Hashtags cannot be empty, '#' should not be detected as a valid hashtag.@@")

    def test08_ht_detection_3(self):
        self._assert([".#c."], {"c": 1})

    def test09_ht_detection_4(self):
        self._assert(["-#d-"], {"d": 1})

    def test10_ht_detection_5(self):
        self._assert(["#e1"], {"e1": 1})

    def test11_ht_detection_6(self):
        self._assert([" #f2 "], {"f2": 1})

    def test12_ht_detection_7(self):
        self._assert([".#g3."], {"g3": 1})

    def test13_ht_detection_8(self):
        self._assert(["-#h4-"], {"h4": 1})

    def test14_ht_detection_neg1(self):
        self._assert(["You are my #1!"], {}, "@@Hashtags have to start with a letter, '#1' should not be detected as a valid hashtag.@@")

    def test15_ht_detection_neg2(self):
        self._assert(["##aa"], {"aa": 1})

    def test16_multiple_1(self):
        self._assert(["#a #b"], {"a": 1, "b": 1})

    def test17_multiple_2(self):
        self._assert([" #c #d "], {"c": 1, "d": 1})

    def test18_multiple_3(self):
        self._assert([" #e #e "], {"e": 2})

    def test19_multiple_4(self):
        self._assert(["#a #f", " #b #f", "#f #c"], {"a": 1, "b": 1, "c": 1, "f": 3})

    def test20_multiple_3(self):
        self._assert(["#a#a"], {"a": 2})

    def test19_case_sensitive(self):
        self._assert([" #a #A "], {"a": 1, "A": 1})
