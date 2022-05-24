#!/usr/bin/env python3

from unittest import TestCase
from public.script import Matrix


class PublicTestSuite(TestCase):

    def assertFailedInit(self, A):
        with self.assertRaises(AssertionError) as ctx:
            A = Matrix(A)

    def test0_empty_list(self):
        self.assertFailedInit([])

    def test1_wrong_input(self):
        self.assertFailedInit("sdf")

    def test2_wrong_input(self):
        self.assertFailedInit(["sdf"])

    def test3_wrong_input(self):
        self.assertFailedInit([[]])

    def test4_wrong_input(self):
        self.assertFailedInit([["dd"]])

    def test5_wrong_input(self):
        self.assertFailedInit([1,2,3])

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
