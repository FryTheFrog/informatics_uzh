from unittest import TestCase
from matrix import Matrix

class PublicTestSuite(TestCase):

    def assertFailedInit(self, A):
        with self.assertRaises(AssertionError) as ctx:
            A = Matrix(A)

    def test0_empty_list(self):
        self.assertFailedInit([])

    def test1_wrong_input(self):
        self.assertFailedInit("sdf")

    def test2_wrong_input(self):
        self.assertFailedInit(["sdf"])

    def test3_wrong_input(self):
        self.assertFailedInit([[]])

    def test4_wrong_input(self):
        self.assertFailedInit([["dd"]])

    def test5_wrong_input(self):
        self.assertFailedInit([1,2,3])

    def test6_wrong_input(self):
        self.assertFailedInit([[1,2], [1,2], [1]])

    def test_add(self):
        A = Matrix([[3,2], [0,1]])
        B = Matrix([[1,3], [2,0]])
        actual = A + B
        expected = Matrix([[4,5], [2,1]])
        self.assertEqual(actual, expected)

    def test_mult(self):
        A = Matrix([[3,2,1], [1,0,2]])
        B = Matrix([[1,2], [0,1], [4,0]])
        actual = A * B
        expected = Matrix([[7,8], [9,2]])
        self.assertEqual(actual, expected)