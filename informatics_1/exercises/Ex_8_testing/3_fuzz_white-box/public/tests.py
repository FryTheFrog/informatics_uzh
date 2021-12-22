#!/usr/bin/env python3
from unittest import TestCase
from public.script import calculate_factorial

class MyTests(TestCase):
    def test_none(self):
        actual = calculate_factorial(None)
        self.assertEqual(None, actual)
