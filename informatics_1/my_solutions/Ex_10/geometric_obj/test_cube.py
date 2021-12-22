from unittest import TestCase
from cube import Cube
from cone import Cone
from cylinder import Cylinder


class CubeTest(TestCase):

    # test getter for color
    def test_cube_get_color(self):
        cube = Cube(10, "red", True)
        actual = cube.get_color()
        self.assertEqual(actual, "red")

    def test_cone_get_color(self):
        cone = Cone(8, 6, 10, "yellow", False)
        actual = cone.get_color()
        self.assertEqual(actual, "yellow")

    def test_cylinder_get_color(self):
        cylinder = Cylinder(3.5, 6.3, "blue", True)
        actual = cylinder.get_color()
        self.assertEqual(actual, "blue")
    
    # test getter for area
    def test_cube_get_area(self):
        cube = Cube(10, "red", True)
        actual = cube.get_area()
        expected = 600
        self.assertEqual(actual, expected)

    def test_cone_get_area(self):
        cone = Cone(8, 6, 10, "yellow", False)
        actual = cone.get_area()
        expected = 452.16
        self.assertEqual(actual, expected)

    def test_cylinder_get_area(self):
        cylinder = Cylinder(3.5, 6.3, "blue", True)
        actual = cylinder.get_area()
        expected = 215.4
        self.assertEqual(actual, expected)
    
    # test getter for volume
    def test_cube_get_vol(self):
        cube = Cube(10, "red", True)
        actual = cube.get_volume()
        expected = 1000
        self.assertEqual(actual, expected)

    def test_cone_get_vol(self):
        cone = Cone(8, 6, 10, "yellow", False)
        actual = cone.get_volume()
        expected = 401.92
        self.assertEqual(actual, expected)

    def test_cylinder_get_vol(self):
        cylinder = Cylinder(3.5, 6.3, "blue", True)
        actual = cylinder.get_volume()
        expected = 242.33
        self.assertEqual(actual, expected)