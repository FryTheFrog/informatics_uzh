#!/usr/bin/env python3
from unittest import TestCase

from public import script

class PublicTestSuite(TestCase):

    def test_one(self):
        script.n = 1
        res = script.fizz_buzz()
        self.assertEqual(res, 1)

    def test_three(self):
        script.n = 3
        res = script.fizz_buzz()
        self.assertEqual(res, "Fizz")

    def test_five(self):
        script.n = 5
        res = script.fizz_buzz()
        self.assertEqual(res, "Buzz")

    def test_fifteen(self):
        script.n = 15
        res = script.fizz_buzz()
        self.assertEqual(res, "FizzBuzz")

