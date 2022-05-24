#!/usr/bin/env python3

from unittest import TestCase
from script import WordLogic


class PublicTestSuite(TestCase):
    def test_example(self):
        w = WordLogic(10, 7)
        words = w.word_selection()
        self.assertEqual(len(words), w.num_words)
