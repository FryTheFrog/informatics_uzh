#!/usr/bin/env python3

from unittest import TestCase

from public import script

n = "079266313"
wa_nrs = [
    # 8 possibilities for indices (with 8 different numbers)
    "0779266313", "0796266313", "0792566313", "0792646313", "0792663313", "0792663213", "0792663113", "0792663130",
    # 2 further possibilities for the remaining 2 missing digit options
    "0789266313", "0792696313",
    # some added other numbers
    "0781343143", "0791343123", "0761343143", "0773425678"
]

class PrivateTestSuite(TestCase):


    def _assert(self, nrs, expected):
        script.wa_nrs = nrs
        actual = sorted(script.get_possible_nrs(n))
        m = f"@@The expected phone numbers are {expected} but {actual} have been found.@@"
        self.assertEqual(expected, actual, m)

    # -all locations
    # -all nrs
    # -different length of returned list: 0, 1, 3, 10

    def test0(self):
        expected = []
        self._assert([], expected)

    def test_each_single_nr_and_index(self):
        for wa_nr in wa_nrs[:10]:
            expected = [wa_nr]
            self._assert([wa_nr] + wa_nrs[-4:], expected)

    def test3_different_nrs(self):
        expected = sorted(wa_nrs[:3])
        self._assert(wa_nrs[:3] + wa_nrs[-4:], expected)

    def test10(self):
        expected = sorted(wa_nrs[:10])
        self._assert(wa_nrs, expected)
