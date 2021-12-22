from unittest import TestCase
from shop import Shop
from clothing_store import ClothingStore
from bakery import Bakery

class TestShops(TestCase):

    def test_bakery_loan(self):
        bakery = Bakery(1000)
        bakery.take_loan(0.1, 1000)
        actual = bakery.pay_rent_and_loan(100)
        self.assertEqual(280.0, actual)

    def test_bakery_already_has_a_loan(self):
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