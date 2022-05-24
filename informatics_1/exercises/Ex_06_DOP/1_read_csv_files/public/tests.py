#!/usr/bin/env python3

from unittest import TestCase
from public.script import read_csv

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

class PublicTestSuite(TestCase):

    def test_example_data(self):
        actual = read_csv("public/example.csv")
        expected = [
            ('Age', 'Gender', 'Weight (kg)', 'Height (cm)'),
            ('28', 'Female', '58', '168'),
            ('33', 'Male', '', '188')]
        self.assertEqual(expected, actual)
