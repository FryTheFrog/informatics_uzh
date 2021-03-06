
from unittest import TestCase
# catch potential exception from import
try:
    from public.cylinder import Cylinder
except Exception:
    # Just make sure that all tests are still executed to have a stable number
    # of exercise points. An appropriate warning is generated by the smoke tests.
    pass


class cylinderTest(TestCase):
    cylinder = None
    object_type = "cylinder"

    @classmethod
    def setUpClass(cls):
        cls.cylinder = Cylinder(10, 5, "blue", True)

    @classmethod
    def tearDownClass(cls):
        cls.cylinder = None

    def test_0_get_color(self):
        try:
            actual = self.cylinder.get_color()
            expected = "blue"
            message = f"@@For the given {self.object_type} object initiated with {expected} color, expected color return was {expected} but {actual} is found@@"
            self.assertEqual(actual, expected, message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_1_set_color(self):
        try:
            expected = "red"
            self.cylinder.set_color(expected)
            actual = self.cylinder.get_color()
            message = f"@@For the given {self.object_type} object with {expected} color, expected color return was {expected} but {actual} is found@@"
            self.assertEqual(actual, expected, message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_2_get_radius(self):
        try:
            expected = 10
            actual = self.cylinder.get_radius()
            message = f"@@For the {self.object_type} object initiated with raidus 10, expected radius return was 10 but {actual} is found@@"
            self.assertEqual(actual, expected, message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_3_get_height(self):
        try:
            expected = 5
            actual = self.cylinder.get_height()
            message = f"@@For the {self.object_type} object initiated with height 5, expected height return was 5 but {actual} is found@@"
            self.assertEqual(actual, expected, message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_4_get_area(self):
        try:
            expected = 942
            actual = self.cylinder.get_area()
            message = f"@@For the {self.object_type} object initiated with cylinder(10,5,red,True) expected area return was {expected} but {actual} is found@@"
            self.assertAlmostEqual(actual, expected, delta=0.01, msg=message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_5_get_volume(self):
        try:
            expected = 1570
            actual = self.cylinder.get_volume()
            message = f"@@For the {self.object_type} object initiated with cylinder(10,5,red,True) expected volume return was {expected} but {actual} is found@@"
            self.assertAlmostEqual(actual, expected, delta=0.01, msg=message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_6_get_filled(self):
        try:
            actual = self.cylinder.get_filled()
            message = f"@@For the {self.object_type} object initiated with True filled, expected filled return was True but {actual} is found@@"
            self.assertTrue(actual, message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)

    def test_7_set_filled(self):
        try:
            self.cylinder.set_filled(False)
            actual = self.cylinder.get_filled()
            message = f"@@For the {self.object_type} object with False filled, expected filled return was False but {actual} is found@@"
            self.assertFalse(actual, message)
        except Exception as e:
            message = "@@An {} error is raised. Please see the details : {}@@".format(
                type(e).__name__, ''.join(str(e) for e in e.args))
            self.fail(message)
