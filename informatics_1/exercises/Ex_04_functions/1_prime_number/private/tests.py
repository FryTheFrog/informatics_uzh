from unittest import TestCase
from public.script import is_prime

class PrivateTestSuite(TestCase):

    def _assert_positive(self, n):
        m = "@@Incorrect for {}!@@".format(n)
        expected = "{} is prime".format(n)
        self.assertEqual(expected, is_prime(n), m)

    def _assert_negative(self, a, b):
        n = a * b
        m = "@@Incorrect for {}!@@".format(n)
        expected = "{} is not a prime number ({} * {} = {})".format(n, a, b, n)
        self.assertEqual(expected, is_prime(n), m)

    def test_imports(self):
        import inspect
        import re
        from public import script
        source = inspect.getsource(script)
        m = "@@The solution seems to import external libraries, please remove all of these.@@"
        for l in source.splitlines():
            print(l)
            self.assertFalse(re.match(r"^\s*(?:from|import)\s+(\w+(?:\s*,\s*\w+)*)", l.strip()), m)


    ###############

    def test_1(self):
        m = "@@1 is not a prime number, it is the multiplicative identity!@@"
        expected = "1 is the multiplicative identity"
        self.assertEqual(expected, is_prime(1), m)

    def test_pos2(self):
        self._assert_positive(2)

    def test_pos3(self):
        self._assert_positive(3)

    def test_pos4(self):
        self._assert_positive(5)

    def test_pos5(self):
        self._assert_positive(7)

    def test_pos6(self):
        self._assert_positive(11)

    def test_pos7(self):
        self._assert_positive(13)

    def test_pos8(self):
        self._assert_positive(349)

    def test_pos9(self):
        self._assert_positive(773)

    ###############

    def test_neg1(self):
        self._assert_negative(2, 3)

    def test_neg2(self):
        self._assert_negative(2, 5)

    def test_neg3(self):
        self._assert_negative(3, 5)

    def test_neg4(self):
        self._assert_negative(2, 7)

    def test_neg5(self):
        self._assert_negative(3, 7)

    def test_neg6(self):
        self._assert_negative(5, 7)

    def test_neg7(self):
        self._assert_negative(2, 11)

    def test_neg8(self):
        self._assert_negative(3, 11)

    def test_neg9(self):
        self._assert_negative(5, 11)
