#!/usr/bin/env python3
from unittest import TestCase

# catch potential exception from import
from public import script

exception_import = None
try:
    from public.script import calculate_factorial, fuzzer, run
except Exception as e:
    exception_import = e

# TODO: accept also error messages without the "XxxError: " part or change description

class PrivateTestSuite(TestCase):

    def _fail_on_import_problem(self):
        if exception_import:
            m = "@@Import of your implementation failed: {}@@".format(
                type(exception_import).__name__)
            self.fail(m)

    def _assertFail(self, inp, expected_exception_type,
                    expected_exception_message, m):
        self._fail_on_import_problem()

        try:
            calculate_factorial(inp)
        except Exception as actual_exception:
            actual_exception_type = type(actual_exception)
            if expected_exception_type != actual_exception_type or expected_exception_message != str(
                    actual_exception):
                self.fail(m)
        else:
            m = "@@Unexpectedly, a hidden test run did not fail with your implementation: {}@@".format(
                m)
            self.fail(m)

    def _assert_factorial(self, inp, expected, m):
        actual = calculate_factorial(inp)
        self.assertEqual(expected, actual, m)

    def _assert_run(self, min_length, max_length, char_start, char_end, trials, expected, m):
        script.min_length_global = min_length
        script.max_length_global = max_length
        script.char_start_global = char_start
        script.char_end_global = char_end
        actual = run(trials)
        self.assertEqual(expected, actual, m)

    # tests for fuzzer()
    def test01_correct_length(self):
        actual = fuzzer(1, 1, 1, 1)
        self.assertEqual(1, len(actual),
                         "@@Fuzzer does not return a string within min and max length@@")

    def test02_correct_character(self):
        char_nr = ord("a")
        actual = fuzzer(1, 1, char_nr, char_nr)
        self.assertEqual("a", actual,
                         "@@Fuzzer(1, 1, {}, {}) should return \"a\"@@".format(char_nr, char_nr))

    # this test can fail with a minimal probability
    def test03_correct_length2(self):
        char_nr = 70
        min_length = 1
        max_length = 3
        actual = [fuzzer(min_length, max_length, char_nr, char_nr) for i in
                  range(100000)]
        expected = [chr(char_nr) * i for i in range(min_length, max_length + 1)]
        self.assertTrue(set(expected).issubset(set(actual)),
                        "@@Fuzzer does not return a string within min and max length or with incorrect characters@@")

    # this test can fail with a minimal probability
    def test04_correct_character2(self):
        char_min = 80
        char_max = 82
        min_length = 3
        max_length = 3
        actual = [fuzzer(min_length, max_length, char_min, char_max) for i in
                  range(100000)]
        expected = [chr(i) * min_length for i in range(char_min, char_max + 1)]
        self.assertTrue(set(expected).issubset(set(actual)),
                        "@@Fuzzer returns a string with incorrect characters or strings of wrong lengths@@")

    # tests factorial()
    def test05_None(self):
        self._assert_factorial(None, None,
                               "@@If the input is None, None should be returned@@")

    def test06_negative_numbers_integer(self):
        self._assertFail(-1, ValueError, "ValueError: number negative",
                         "@@Factorial: For negative integers as input a ValueError should be raised with the message \"ValueError: number negative\"@@")

    def test07_negative_numbers_string(self):
        self._assertFail("-1", ValueError, "ValueError: number negative",
                         "@@Factorial: For negative string numbers as input a ValueError should be raised with the message \"ValueError: number negative\"@@")

    def test08_number_too_large_integer(self):
        self._assertFail(11, ValueError, "ValueError: number too large",
                         "@@Factorial: For integer numbers larger than 10 a ValueError should be raised with the message \"ValueError: number too large\"@@")

    def test09_number_too_large_string(self):
        self._assertFail("11", ValueError, "ValueError: number too large",
                         "@@Factorial: For string numbers larger than 10 a ValueError should be raised with the message \"ValueError: number too large\"@@")

    def test10_string(self):
        self._assertFail("s", TypeError, "TypeError: string",
                         "@@Factorial: For strings a TypeError should be raised with the message \"TypeError: string\"@@")

    def test11_case_zero_integer(self):
        self._assert_factorial(0, 1, "@@The calculation for the factorial of 0 with integer input is wrong@@")

    def test12_case_zero_string(self):
        self._assert_factorial("0", 1, "@@The calculation for the factorial of 0 with string input is wrong@@")

    def test13_larger_than_zero_integer(self):
        self._assert_factorial(7, 5040, "@@The calculation for the factorial of 7 with integer input is wrong@@")

    def test14_larger_than_zero_string(self):
        self._assert_factorial("7", 5040, "@@The calculation for the factorial of 7 with string input is wrong@@")

    # test for run()
    def test15_empty_list(self):
        actual = run(0)
        self.assertEqual([], actual,
                         "@@Run should return an empty list if trials is equal to 0@@")

    # very small probability that this test fails even though solution is correct
    # probability that a negative number is produced 1/11 * 7/11 = 0.05785123967
    # probability that no negative number is produced 1 - (1/11 * 7/11) = 0.9421487603
    # probability that no negative number is produced in 10000: (1 - (1/11 * 7/11))^10000 = 1.5660665×10−259
    def test16_Value_Error_and_message1(self):
        script.min_length_global = 2
        script.max_length_global = 2
        script.char_start_global = 45
        script.char_end_global = 55

        actual = run(10000)
        expected = (1, "ValueError: number negative")
        self.assertTrue(expected in actual,
                        "@@Run should return [(1, \"ValueError: number negative\")] for trials = 1 and calculate_factorial inputs which are negative numbers@@")


    def test17_ValueError_message2(self):
        expected = [(1, "ValueError: number too large")]
        self._assert_run(2, 2, 50, 50, 1, expected, "@@Run should return [(1, \"ValueError: number too large\")] for trials = 1 and calculate_factorial inputs larger than 10@@")

    def test18_TypeError_message(self):
        expected = [(1, "Other error")]
        self._assert_run(1, 1, 65, 65, 1, expected, "@@Run should return [(1, \"Other error\")] for trials = 1 and calculate_factorial inputs which are a string but not a number@@")

    def test19_correct_execution(self):
        expected = [(0, "")]
        self._assert_run(1, 1, 50, 50, 1, expected, "@@Run should return [(0, \"\")] for trials = 1 and calculate_factorial inputs which are a string number@@")
