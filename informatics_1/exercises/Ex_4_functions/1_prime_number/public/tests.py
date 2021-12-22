#!/usr/bin/env python3

from unittest import TestCase
from public.script import is_prime


class PublicTestSuite(TestCase):

    def test_positive(self):
        m = "Incorrect for 3!"
        self.assertEqual("3 is prime", is_prime(3), m)

    def test_positive(self):
        m = "Incorrect for 12!"
        self.assertEqual("12 is not a prime number (2 * 6 = 12)", is_prime(12), m)

