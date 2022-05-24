#!/usr/bin/env python3

from unittest import TestCase
from public.script import fine_calculator


class SampleFineCalculatorTest(TestCase):
    coefficients = {
        "urban": 1,
        "expressway": 0.8,
        "motorway": 0.5
    }

    speed_limits = {
        "urban": 50,
        "expressway": 100,
        "motorway": 120
    }

    def calculate_expected(self, area, speed):
        speed_limit = self.speed_limits[area]
        if (speed <= speed_limit):
            return 0
        else:
            coefficient = self.coefficients[area]
            difference = speed_limit - speed
            difference_ratio = (difference / speed_limit)*100
            fine = coefficient * difference_ratio**2
            return round(fine)

    def _assert(self, area, speed):
        try:
            actual = fine_calculator(area, speed)
            expected = self.calculate_expected(area, speed)
        except Exception as e:
            self.fail("An unexpected error is raised")

        self.assertEqual(expected, actual)

    def test_01_return_type_valid(self):
        area = "urban"
        speed = 60
        actual = fine_calculator(area, speed)
        self.assertIsInstance(actual, int)

    # Urban area speed is lower than the limit of 50
    def test_02_urban_lower_limit(self):
        area = "urban"
        speed = 49
        self._assert(area, speed)

    # Urban area speed is on the limit of 50
    def test_03_urban_on_limit(self):
        area = "urban"
        speed = 50
        self._assert(area, speed)

    # Urban area speed is beyond the limit of 50
    def test_04_urban_beyond_limit_01(self):
        area = "urban"
        speed = 51
        self._assert(area, speed)

    # Urban area speed is beyond the limit of 50
    def test_05_urban_beyond_limit_02(self):
        area = "urban"
        speed = 100
        self._assert(area, speed)

    # Expressway area below the limit. Limit is 100
    def test_06_expressway_below_limit(self):
        area = "expressway"
        speed = 99
        self._assert(area, speed)

    # Expressway area speed is on the limit of 100
    def test_07_expressway_on_limit(self):
        area = "expressway"
        speed = 100
        self._assert(area, speed)

    # Expressway area speed is beyond the limit of 100
    def test_08_expressway_beyond_limit_01(self):
        area = "expressway"
        speed = 101
        self._assert(area, speed)

    # Expressway area speed is beyond the limit of 100
    def test_09_expressway_beyond_limit_02(self):
        area = "expressway"
        speed = 140
        self._assert(area, speed)

     # Motorway area below the limit. Limit is 120
    def test_10_motorway_below_limit(self):
        area = "motorway"
        speed = 119
        self._assert(area, speed)

    # Motorway area on the limit. Limit is 120
    def test_11_motorway_on_limit(self):
        area = "motorway"
        speed = 120
        self._assert(area, speed)

    # Motorway area beyond the limit. Limit is 120
    def test_12_motorway_beyond_limit_01(self):
        area = "motorway"
        speed = 121
        self._assert(area, speed)

    # Motorway area beyond the limit. Limit is 120
    def test_13_motorway_beyond_limit_02(self):
        area = "motorway"
        speed = 150
        self._assert(area, speed)

    # Urban area below the limit, float input
    def test_14_urban_below_limit_float(self):
        area = "urban"
        speed = 49.99
        self._assert(area, speed)

    # Urban area on the limit, float input
    def test_15_urban_on_limit_float(self):
        area = "urban"
        speed = 50.0
        self._assert(area, speed)

    # Urban area beyond the limit, float input
    def test_16_urban_on_beyond_float(self):
        area = "urban"
        speed = 150.01
        self._assert(area, speed)

    # Urban area invalid negative speed
    def test_17_invalid_speed_negative(self):
        area = "urban"
        speed = -3
        actual = fine_calculator(area, speed)
        expected = "Invalid Speed Value"
        self.assertEqual(actual, expected)

    # Urban area invalid string speed
    def test_18_invalid_speed_string(self):
        area = "urban"
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Speed Type"
        self.assertEqual(actual, expected)

    # Invalid area with dict type
    def test_19_invalid_area_type_dict(self):
        area = ["urban"]
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Area Type"
        self.assertEqual(actual, expected)

    # Invalid area with int type
    def test_20_invalid_area_type_int(self):
        area = 10
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Area Type"
        self.assertEqual(actual, expected)

    # Invalid area with int type
    def test_21_invalid_area_value(self):
        area = "Zurich"
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Area Value"
        self.assertEqual(actual, expected)
