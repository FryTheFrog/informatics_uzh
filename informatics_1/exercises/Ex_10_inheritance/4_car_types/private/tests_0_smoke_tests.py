#!/usr/bin/env python3

import builtins, sys
from unittest import TestCase

# replace input implementation
class YouCannotUseInputInACCESSException(Exception): pass
def crashing_input(prompt):
    raise YouCannotUseInputInACCESSException()
builtins.input_orig = builtins.input
builtins.input = crashing_input

# catch potential exception from import
import_ex = None
try:
    from public.combustion_car import CombustionCar
    from public.electric_car import ElectricCar
    from public.hybrid_car import HybridCar
except:
    import_ex = sys.exc_info()[0].__name__

class PrivateSmokeTestSuite(TestCase):

    def _run_example(self):
        # script
        c = CombustionCar(40.0, 8.0)
        c.get_remaining_range()  # 500
        c.drive(25.0)
        c.get_gas_tank_status()  # (38.0, 40.0)
        with self.assertRaises(Warning):
            c.drive(1000.0)  # fuel is depleted

        e = ElectricCar(25.0, 500.0)
        e.drive(100.0)
        e.charge(2.0)
        e.get_battery_status()  # (22.0, 25)

        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        h.drive(600.0)  # depletes fuel, auto-switch
        h.get_gas_tank_status()  # (0.0, 40.0)
        h.get_battery_status()  # (20.0, 25.0)

        # test1
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

        # test2
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test0_example(self):
        if import_ex:
            m = "@@Failed to import at least one of the implementation scripts due to a '{}'.@@".format(import_ex)
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
