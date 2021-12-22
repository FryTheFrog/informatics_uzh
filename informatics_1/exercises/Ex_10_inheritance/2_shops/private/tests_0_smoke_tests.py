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
    from public.bakery import Bakery
    from public.clothing_store import ClothingStore
    from public.shopping_center import ShoppingCenter
except:
    import_ex = sys.exc_info()[0].__name__

class PrivateSmokeTestSuite(TestCase):

    def _run_example(self):
        # script
        bakery = Bakery(1000)  # (capital, loan, interest, initial_loan_amount, dough, bread) = (1000, 0, 0, 0, 0, 0)
        bakery.take_loan(0.1, 1000)  # (2000, 1000, 0.1, 1000, 0, 0)
        amount_paid_b = bakery.pay_rent_and_loan(100)  # (1720.0, 900, 0.1, 1000, 0, 0)
        bakery.procure(1, 100)  # (1620.0, 900, 0.1, 1000, 100, 0)
        bakery.produce(1)  # (1520.0, 900, 0.1, 1000, 0, 100)
        bakery.sell(6, 50)  # (1745.0, 900, 0.1, 1000, 0, 50)
        with self.assertRaises(Warning):
            bakery.take_loan(0.1, 1000)

        clothing_store = ClothingStore(2000)  # (capital, loan, interest, initial_loan_amount, clothing_pieces) = (2000, 0, 0, 0, 0)
        clothing_store.take_loan(0.1, 1000)  # (3000, 1000, 0.1, 1000, 0)
        amount_paid_c = clothing_store.pay_rent_and_loan(100)  # (2700.0, 900, 0.1, 1000, 0)
        clothing_store.procure(1, 100)  # (2620.0, 900, 0.1, 1000, 100)
        clothing_store.sell(10, 10)  # (2720.0, 900, 0.1, 1000, 90)

        bakery_two = Bakery(1000)
        shopping_center = ShoppingCenter(10000, [bakery_two])  # capital = 10000
        shopping_center.add_shop(ClothingStore(2000))  # capital = 10000
        shopping_center.grant_loan(bakery_two, 0.05, 1000)  # capital = 9000
        shopping_center.collect_rent_and_loan(100)  # capital = 9330

        # test1
        bakery = Bakery(1000)
        bakery.take_loan(0.1, 1000)
        actual = bakery.pay_rent_and_loan(100)
        self.assertEqual(280.0, actual)

        # test2
        bakery = Bakery(1000)
        bakery.take_loan(0.1, 1000)
        try:
            bakery.take_loan(0.05, 1000)
        except Warning:
            pass
        except:
            self.fail("Wrong error raised")
        else:
            self.fail("No warning raised")

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
