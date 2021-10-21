from unittest import TestCase

import script

class test_suite(TestCase):
    def test_one(self):
        script.pwd = 'abAB12++'
        res = script.pwd_check()
        self.assertEqual(res, True)
    def test_two(self):
        script.pwd = 'abAB12**'
        res = script.pwd_check()
        self.assertEqual(res, True)
    def test_three(self):
        script.pwd = 'abAB12##'
        res = script.pwd_check()
        self.assertEqual(res, False)
    def test_four(self):
        script.pwd = 'abab12++'
        res = script.pwd_check()
        self.assertEqual(res, False)
    def test_five(self):
        script.pwd = 'ab'
        res = script.pwd_check()
        self.assertEqual(res, False)