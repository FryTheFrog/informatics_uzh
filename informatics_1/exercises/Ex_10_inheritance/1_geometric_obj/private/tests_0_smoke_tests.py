#!/usr/bin/env python3

import builtins
import sys
from unittest import TestCase

# replace input implementation


class YouCannotUseInputInACCESSException(Exception):
    pass


def crashing_input(prompt):
    raise YouCannotUseInputInACCESSException()


builtins.input_orig = builtins.input
builtins.input = crashing_input

# catch potential exception from import
import_ex = None
try:
    from public.cone import Cone
    from public.cube import Cube
    from public.cylinder import Cylinder
except:
    import_ex = sys.exc_info()[0].__name__


class PrivateSmokeTestSuite(TestCase):

    def _run_example(self):
        # test1
        cube = Cube(10, "red", True)
        actual = cube.get_color()
        self.assertEqual(actual, "red")

        # test2
        cone = Cone(10, 5, 6.4, "yellow", False)
        actual = cone.get_color()
        self.assertEqual(actual, "yellow")

        # test3
        cylinder = Cylinder(3.5, 6.3, "blue", True)
        actual = cylinder.get_color()
        self.assertEqual(actual, "blue")

    def test0_example(self):
        if import_ex:
            m = "@@Failed to import at least one of the implementation scripts due to a '{}'.@@".format(
                import_ex)
            self.fail(m)

        try:
            self._run_example()
        except AssertionError:
            m = "@@Running the provided example has an incorrect result. Make sure that " +\
                "the public script and test suite pass, before you attempt any submissions.@@"
            self.fail(m)
        except:
            m = "@@Failed to run the provided example. Make sure that the public script and test " +\
                "suite passes, before you attempt any submissions.@@"
            self.fail(m)

    def test1_repeatability(self):
        try:
            self._run_example()
            self._run_example()
        except:
            m = "@@Failed to run the provided script and test suite a second time. This might be caused by shared " +\
                "class variables that introduce unexpected side effects. We highly encourage you to " +\
                "add your own tests to the public test suite before you attempt any submissions.@@"
            self.fail(m)
