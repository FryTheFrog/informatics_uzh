#!/usr/bin/env python3

from unittest import TestCase
from public.script import visualize

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".


class PublicTestSuite(TestCase):

    def test(self):
        _in = []
        _in.extend(10 * [(True, 1, 'Some Name', 'female', 38, 71.2833)])
        _in.extend(13 * [(False, 1, 'Some Name', 'female', 38, 71.2833)])
        _in.extend(22 * [(True, 2, 'Some Name', 'female', 38, 71.2833)])
        _in.extend(57 * [(False, 2, 'Some Name', 'female', 38, 71.2833)])
        _in.extend(151 * [(True, 3, 'Some Name', 'female', 38, 71.2833)])
        _in.extend(276 * [(False, 3, 'Some Name', 'female', 38, 71.2833)])

        actual = visualize((
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            _in
        ))
        expected = "\n".join([
            "== 1st Class ==",
            "Total |*                   | 4.3%",
            "Alive |*********           | 43.5%",
            "== 2nd Class ==",
            "Total |***                 | 14.9%",
            "Alive |******              | 27.8%",
            "== 3rd Class ==",
            "Total |****************    | 80.7%",
            "Alive |*******             | 35.4%"
        ])
        if type(actual) == str:
            actual = actual.replace(",", ".").replace("\r\n", "\n").strip()
        self.assertEqual(expected, actual, "")
