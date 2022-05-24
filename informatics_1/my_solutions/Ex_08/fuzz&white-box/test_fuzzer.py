from unittest import TestCase
from fuzzer import calculate_factorial


class MyTests(TestCase):
    def test_none(self):
        actual = calculate_factorial(None)
        self.assertEqual(None, actual)

    def test_invalid_string(self):
        with self.assertRaisesRegex(TypeError, "TypeError: string"):
            calculate_factorial("tree")

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "ValueError: number negative"):
            calculate_factorial("-1")

    def test_negative2(self):
        with self.assertRaisesRegex(ValueError, "ValueError: number negative"):
            calculate_factorial(-8)

    def test_too_large(self):
        with self.assertRaisesRegex(ValueError, "ValueError: number too large"):
            calculate_factorial("11")

    def test_too_large2(self):
        with self.assertRaisesRegex(ValueError, "ValueError: number too large"):
            calculate_factorial(11)

    def test_val(self):
        actual = calculate_factorial("0")
        self.assertEqual(1, actual)

    def test_val1(self):
        actual = calculate_factorial(0)
        self.assertEqual(1, actual)

    def test_val2(self):
        actual = calculate_factorial(2)
        self.assertEqual(2, actual)

    def test_val3(self):
        actual = calculate_factorial("4")
        self.assertEqual(24, actual)

    def test_val4(self):
        actual = calculate_factorial(9)
        self.assertEqual(362880, actual)
