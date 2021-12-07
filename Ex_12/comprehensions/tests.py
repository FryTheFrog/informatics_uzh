#!/usr/bin/env python3
from unittest import TestCase
import script as script

class PublicTestSuite(TestCase):

    def test_example(self):
        self.assertTrue(len(script.words_with_length(12)) == 208)
