#!/usr/bin/env python3
from unittest import TestCase
from public.script import calculate_factorial

class MyTests(TestCase):

    def _assert(self, inp, expected):
        actual = calculate_factorial(inp)
        self.assertEqual(expected, actual)

    # tests calculate_factorial
    def test_None(self):
        self.assertEqual(None, calculate_factorial(None))

    def test_negative_numbers_integer(self):
        self.assertRaises(ValueError, calculate_factorial, -1)

    def test_negative_numbers_string(self):
        self.assertRaises(ValueError, calculate_factorial, "-1")

    def test_number_too_large_integer(self):
        self.assertRaises(ValueError, calculate_factorial, 11)

    def test_number_too_large_string(self):
        self.assertRaises(ValueError, calculate_factorial, "11")

    def test_string(self):
        self.assertRaises(TypeError, calculate_factorial, "s")

    def test_case_zero_integer(self):
        self._assert(0, 1)

    def test_case_zero_string(self):
        self._assert("0", 1)

    def test_larger_than_zero_integer(self):
        self._assert(7, 5040)

    def test_larger_than_zero_string(self):
        self._assert("7", 5040)