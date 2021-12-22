#!/usr/bin/env python3¨
import inspect
from unittest import TestCase

from public import script

def get_pyramid_string(height):
    script.h = height
    return script.build_string_pyramid()


class PrivateTestSuite(TestCase):

    def _test_pattern(self, height):
        actual = get_pyramid_string(height)
        self._check_multiple_for_loops_used()
        self._test_lines(height, actual)

    def _test_lines(self, height, actual):
        actual_l = actual.split("\n")[:-1] if actual.split("\n")[-1] == "" else actual.split("\n")
        self._check_size(len(actual_l), 2*height -1 if height > 0 else 0, height)
        for i, line in enumerate(actual_l):
            self._test_line(height - (1+i) % height if i+1 > height else i+1, i+1, line, height)
            
    def _test_line(self, lineloc, line_nr, actual, height):
        expected = ""
        for i in range(1, lineloc+1):
            expected += str(i)
            if i < lineloc:
                expected += "*"

        msg = f"@@for a pyramid of h={height}, the {line_nr}. line should be '{expected}', but was '{actual}'.@@"
        self.assertEqual(expected, actual, msg)
    
    def _check_size(self, num_lines, expected, height):
        msg = f"@@for a pyramid of h={height}, the number of lines should be '{expected}', but there are '{num_lines}'.@@"
        self.assertEqual(expected, num_lines, msg)

    def _check_multiple_for_loops_used(self):
        num_fors = inspect.getsource(script.build_string_pyramid).count("for")
        print(num_fors)
        self.assertGreater(num_fors, 1, "@@Please use more than one for loop@@")

    # test cases

    def test_height_zero(self):
        self._check_multiple_for_loops_used()
        actual = get_pyramid_string(0)
        msg = f"@@for a pyramid of h=0, the string should be empty {''}, but it was '{actual}' .@@"
        self.assertEqual("", actual, msg)

    def test_height_one(self):
        self._test_pattern(1)

    def test_height_three(self):
        self._test_pattern(3)
    
    def test_height_five(self):
        self._test_pattern(5)
    
    def test_height_ten(self):
        self._test_pattern(10)

    def test_height_50(self):
        self._test_pattern(50)
    
    def test_height_100(self):
        self._test_pattern(100)

