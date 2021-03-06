#!/usr/bin/env python3

from unittest import TestCase

# catch potential exception from import
try:
    from public.shopping_center import ShoppingCenter
    from public.bakery import Bakery
    from public.clothing_store import ClothingStore
except Exception:
    # Just make sure that all tests are still executed to have a stable number
    # of exercise points. An appropriate warning is generated by the smoke tests.
    pass

class TestShoppingCenter(TestCase):

    def test00_shopping_center_init(self):
        try:
            bakery = Bakery(2000)
            sut = ShoppingCenter(10000, [bakery])
            capital, shops, debtors = sut.get_status()
        except:
            m = "@@Unexpected error when checking the status of the ShoppingCenter directly after initialization.@@"
            self.fail(m)
        m = "@@Incorrect result when checking the status of a ShoppingCenter directly after initialization.@@"
        self.assertEqual(10000, capital, m)
        self.assertEqual((bakery,), shops, m)
        self.assertEqual((), debtors, m)

    def test01_shopping_center_init(self):
        try:
            sut = ShoppingCenter(10000, [])
            capital, shops, debtors = sut.get_status()
        except Warning:
            pass
        except:
            m = "@@When a shopping center is initialized without a shop, an unexpected error happened.@@"
            self.fail(m)
        else:
            m = "@@When a shopping center is initialized without a shop, a Warning should be raised.@@"
            self.fail(m)


    def test02_shopping_center_len(self):
        try:
            sut = ShoppingCenter(10000, [Bakery(2000), Bakery(1000)])
            actual = len(sut)
        except:
            m = "@@Unexpected error when checking the length of the ShoppingCenter directly after initialization.@@"
            self.fail(m)
        m = "@@Incorrect result when checking the length of a ShoppingCenter directly after initialization.@@"
        self.assertEqual(2, actual, m)

    def test03_shopping_center_add_remove_shops(self):
        try:
            bakery = Bakery(2000)
            sut = ShoppingCenter(10000, [bakery])
        except:
            m = "@@Unexpected error while initializing the ShoppingCenter.@@"
            self.fail(m)
        try:
            clothing_store = ClothingStore(20000)
            sut.add_shop(clothing_store)
        except:
            m = "@@Unexpected error while adding a stop to the ShoppingCenter.@@"
            self.fail(m)
        try:
            sut.remove_shop(bakery)
        except:
            m = "@@Unexpected error while removing a shop from the ShoppingCenter.@@"
            self.fail(m)
        capital, shops, debtors = sut.get_status()
        m = "@@After adding and removing shops, ShoppingCenter contains incorrect shops.@@"
        self.assertEqual((clothing_store,), shops, m)


    def test04_shopping_center_grant_loan(self):
        try:
            bakery = Bakery(2000)
            sut = ShoppingCenter(10000, [bakery])
            sut.grant_loan(bakery, 0.1, 2000)
        except:
            m = "@@Unexpected error while granting a loan to a shop.@@"
            self.fail(m)
        capital, shops, debtors = sut.get_status()
        m = "@@After granting a loan to a shop, the status of the ShoppingCenter is incorrect.@@"
        self.assertEqual(8000, capital, m)
        self.assertEqual((bakery,), debtors, m)
        try:
            capital_bakery, loan, interest, initial_loan_amount, dough, bread = bakery.get_status()
        except:
            m = "@@Unexpected error while accessing the shop status of the bakery to check loan and interest.@@"
            self.fail(m)
        m = "@@Shop does not have the correct status after being granted a loan.@@"
        self.assertEqual(4000, capital_bakery, m)
        self.assertEqual(2000, loan, m)
        self.assertEqual(0.1, interest)

    def test05_shopping_center_grant_loan_only_to_shops(self):
        try:
            bakery = Bakery(2000)
            sut = ShoppingCenter(10000, [bakery])
            foreign_bakery = Bakery(5000)
            sut.grant_loan(foreign_bakery, 0.1, 2000)
        except Warning:
            pass
        except:
            m = "@@Unexpected error while granting a loan to a shop.@@"
            self.fail(m)
        else:
            m = "@@If the ShoppingCenter tries to grant a loan to a shop which does not belong the ShoppingCenter, a Warning should be raised.@@"
            self.fail(m)

    def test06_shopping_center_grant_loan_more_than_capital(self):
        try:
            bakery = Bakery(4000)
            sut = ShoppingCenter(10000, [bakery])
            sut.grant_loan(bakery, 0.1, 20000)
        except Warning:
            pass
        except:
            m = "@@Unexpected error while granting a loan to a shop.@@"
            self.fail(m)
        else:
            m = "@@If the ShoppingCenter tries to grant a loan of higher amount than the capital, an error should be raised.@@"
            self.fail(m)

    def test07_shopping_center_collect_rent_and_loan(self):
        try:
            bakery = Bakery(4000)
            clothing_store = ClothingStore(5000)
            sut = ShoppingCenter(10000, [bakery, clothing_store])
            sut.grant_loan(bakery, 0.05, 2000)
            sut.collect_rent_and_loan(200)
            capital, shops, debtors = sut.get_status()
        except:
            m = "@@Unexpected error while collecting the rent and the loan of shops.@@"
            self.fail(m)
        m = "@@After collecting the rent and loans of the shops, the status of the ShoppingCenter is incorrect.@@"
        expected_capital = 10000 - 2000 + (160 + 200 + 100) + 200
        self.assertEqual(expected_capital, capital, m)
        self.assertEqual((bakery, clothing_store), shops, m)
        self.assertEqual((bakery,), debtors, m)
        try:
            capital_bakery, loan, interest, initial_loan_amount, dough, bread = bakery.get_status()
        except:
            m = "@@Unexpected error while accessing the shop status of the bakery after the shopping center has collected rent and loans from the shops.@@"
            self.fail(m)
        m = "@@After the ShoppingCenter has collected rent and loan from the shops, a bakery does not have the correct status.@@"
        expected_capital_bakery = 4000 + 2000 - (160 + 200 + 100)
        self.assertEqual(expected_capital_bakery, capital_bakery, m)
        self.assertEqual(1800, loan, m)
        self.assertEqual(0.05, interest)


    def test08_shopping_center_remove_debtor(self):
        try:
            bakery = Bakery(10000)
            clothing_store = ClothingStore(5000)
            sut = ShoppingCenter(10000, [bakery, clothing_store])
            sut.grant_loan(bakery, 0.05, 2000)
            for i in range(10):
                sut.collect_rent_and_loan(200)
            capital, shops, debtors = sut.get_status()
        except:
            m = "@@Unexpected error while collecting the rent and the loan of shops.@@"
            self.fail(m)
        m = "@@After a shopping center has collected the rent and loans of the shops 10 times, the debtors should have payed back their loan and be removed from the debtors list.@@"
        expected_capital = 14150.0
        self.assertEqual(expected_capital, capital, m)
        self.assertEqual((bakery, clothing_store), shops, m)
        self.assertEqual((), debtors, m)
