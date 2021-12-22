#!/usr/bin/env python3

import sys
from unittest import TestCase
from numpy import array

# catch potential exception from import
try:
    from public.script import Matrix
except Exception:
    # Just make sure that all tests are still executed to have a stable number of points.
    # An appropriate warning is generated by the smoke tests.
    pass

class PrivateFunctionalTestSuite(TestCase):

    def assert_op(self, A, B, expected, operation="*"):
        A = Matrix(A)
        B = Matrix(B)
        if operation == "*":
            actual = A * B
        else:
            actual = A + B
        msg = f"@@Result should be {Matrix(expected)}, but was {actual}@@"
        self.assertEqual(Matrix(expected), actual, msg)

    def assertFailedInit(self, A):
        with self.assertRaises(AssertionError) as ctx:
            A = Matrix(A)

    def assertFailedOp(self, A, B, operation="*"):
        A = Matrix(A)
        B = Matrix(B)
        with self.assertRaises(AssertionError) as ctx:
            if operation == "*":
                actual = A * B
            else:
                actual = A + B

    # test static methods
    def test0_empty_list(self):
        self.assertFailedInit([])

    def test1_wrong_input(self):
        self.assertFailedInit("sdf")

    def test2_wrong_input(self):
        self.assertFailedInit(((1,2,3)))

    def test3_wrong_input(self):
        self.assertFailedInit([[]])

    def test4_wrong_input(self):
        self.assertFailedInit([["dd"]])

    def test5_wrong_input(self):
        self.assertFailedInit([1, 2, 3])

    def test6_wrong_input(self):
        self.assertFailedInit(1)

    def test7_3_dimensional_input(self):
        self.assertFailedInit([[[1, 2, 3]]])

    def test8_incorrect_input_with_correct_part(self):
        self.assertFailedInit([[], [1, 2]])

    def test9_incorrect_rectangle_dimensions(self):
        self.assertFailedInit([[1, 2, 3], [1, 2]])

    def test10_incorrect_rectangle_dimensions(self):
        self.assertFailedInit([[1], [1, 2]])

    def test11_addition_correct(self):
        self.assert_op([[1]], [[1]], [[2]], "+")

    def test12_addition_correct(self):
        self.assert_op([[1, 2]], [[1, 2]], [[2, 4]], "+")

    def test13_addition_correct3(self):
        self.assert_op([[1, 2], [1, 2]], [[1, 2], [1, 2]], [[2, 4], [2, 4]], "+")

    def test14_addition_not_matching_dimensions(self):
        self.assertFailedOp([[1, 2]], [[1]], "+")

    def test15_addition_not_matching_dimensions(self):
        self.assertFailedOp([[1, 2]], [[1, 2], [1, 2]], "+")

    def test16_addition_not_matching_dimensions(self):
        self.assertFailedOp([[1, 2]], [[1], [2]], "+")

    def test_multiplication_correct1(self):
        self.assert_op([[1]], [[1]], [[1]])

    def test_multiplication_correct2(self):
        self.assert_op([[1, 2]], [[1], [2]], [[5]])

    def test_multiplication_correct3(self):
        self.assert_op([[1, 2], [1, 3]], [[1, 2], [1, 2]], [[3, 6], [4, 8]])

    def test_multiplication_not_matching_dimensions(self):
        self.assertFailedOp([[1]], [[2], [2]])

    def test_multiplication_not_matching_dimensions2(self):
        self.assertFailedOp([[1, 2]], [[2]])





