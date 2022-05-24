#!/usr/bin/env python3

from unittest import TestCase
from public.script import gender_class_rates

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

class PublicTestSuite(TestCase):

    def test_example_data(self):
        actual = gender_class_rates((
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            [
                (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38, 71.2833),
                (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
            ]
        ))
        expected = (
            (None, None, None),
            (50.0, None, 50.0)
        )
        self.assertEqual(expected, actual)