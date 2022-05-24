#!/usr/bin/env python3

from unittest import TestCase
from public.script import process_data


class PublicTestSuite(TestCase):

    def test_example_file(self):
        process_data("public/my_data.txt", "public/my_data_processed.txt")
        expected = "Firstname,Lastname\nBeat,Meier\n,\nBarbara,Suter\nRoland,Berger"
        with open("public/my_data_processed.txt", "r") as f:
            actual = f.read()
        self.assertEqual(expected, actual)

    def test_non_existing_file(self):
        actual = process_data("non_existing_file.txt", "my_data_processed.txt")
        expected = False
        self.assertEqual(expected, actual)

