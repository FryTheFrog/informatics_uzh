#!/usr/bin/env python3

from unittest import TestCase

from public import script


def is_valid(pwd):
    script.pwd = pwd
    return script.is_valid()


class PrivateTestSuite(TestCase):

    def _assertValid(self, pwd):
        actual = is_valid(pwd)
        m = "@@\"{}\" is a valid password!@@".format(pwd)
        self.assertTrue(actual, m)

    def _assertInvalid(self, pwd):
        actual = is_valid(pwd)
        m = "@@\"{}\" is an invalid password!@@".format(pwd)
        self.assertFalse(actual, m)

    def test_valid1(self):
        self._assertValid("aaAA00++")

    def test_valid2(self):
        self._assertValid("aaaAAA000+++")

    def test_valid2(self):
        self._assertValid("aaaaAAAA0000++++")

    def test_invalid_too_log(self):
        self._assertInvalid("aaaaAAAA0000++++x")

    def test_valid3(self):
        self._assertValid("xW+5xW+5")

    def test_invalid_not_enough_lower(self):
        self._assertInvalid("aAAA00++")

    def test_invalid_not_enough_upper(self):
        self._assertInvalid("aaaA00++")

    def test_invalid_not_enough_digits(self):
        self._assertInvalid("aaAAA0++")

    def test_invalid_not_enough_special(self):
        self._assertInvalid("aaAA000+")

    def test_invalid_other_chars(self):
        self._assertInvalid("aaAA00++#")

    def test_valid_all_lower(self):
        for c in "abcdefghijklmnopqrstuvwxyz":
            self._assertValid(c + c + "AA00++")

    def test_valid_all_upper(self):
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self._assertValid(c + c + "aa00++")

    def test_valid_all_digits(self):
        for d in range(10):
            self._assertValid(str(d) + str(d) + "aaAA++")

    def test_valid_all_special(self):
        for d in "+-/*":
            self._assertValid(d + d + "aaAA00")
