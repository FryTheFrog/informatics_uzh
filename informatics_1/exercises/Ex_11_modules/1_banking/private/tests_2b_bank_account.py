#!/usr/bin/env python3
from unittest import TestCase
from public.bank_account import BankAccount


class PrivateBankAccountTests(TestCase):

    def test_defaults(self):
        try:
            sut = BankAccount()
            actual_cur = sut.get_currency()
            actual_balance = sut.get_balance()
        except:
            m = "@@Failed to init a BankAccount and to request currency and balance.@@"
            self.fail(m)
        m = "@@A BankAccount does not report the correct currency when the default should be used.@@"
        self.assertEqual("CHF", actual_cur, m)
        m = "@@A BankAccount does not have the right balance after initialization.@@"
        self.assertAlmostEqual(0, actual_balance, delta=0.001, msg=m)

    def test_defaults_with_diff_currency(self):
        try:
            sut = BankAccount("EUR")
            actual_cur = sut.get_currency()
            actual_balance = sut.get_balance()
        except:
            m = "@@Failed to init a BankAccount and to request currency and balance.@@"
            self.fail(m)
        m = "@@A BankAccount does not report the correct currency when a custom currency should be used.@@"
        self.assertEqual("EUR", actual_cur, m)
        m = "@@A BankAccount does not have the right balance after initialization.@@"
        self.assertAlmostEqual(0, actual_balance, delta=0.001, msg=m)

    def test_fail_init_cur(self):
        try:
            BankAccount("RUB")
        except Warning:
            pass
        except:
            m = "@@The init of a BankAccount fails with an unexpected error when an unknown currency is used.@@"
            self.fail(m)
        else:
            m = "@@The init of a BankAccount does not fail when an unknown currency is used.@@"
            self.fail(m)

    def test_deposit(self):
        try:
            sut = BankAccount("USD")
            sut.deposit(1.23, "USD")
            actual = sut.get_balance()
        except:
            m = "@@Depositing money in the currency of the account fails.@@"
            self.fail(m)
        m = "@@Depositing money in the currency of the account results in an incorrect balance.@@"
        self.assertAlmostEqual(1.23, actual, delta=0.001, msg=m)

    def test_deposit_with_explicit_conversion(self):
        try:
            sut = BankAccount("CAD")
            sut.deposit(2.34, "EUR")
            actual = sut.get_balance()
        except:
            m = "@@Failed to deposit money that requires a conversion.@@"
            self.fail(m)
        m = "@@Incorrect balance when depositting money that requires a conversion.@@"
        self.assertAlmostEqual(3.421, actual, delta=0.001, msg=m)

    def test_deposit_with_implicit_conversion(self):
        try:
            sut = BankAccount("CAD")
            sut.deposit(3.45)
            actual = sut.get_balance()
        except:
            m = "@@Failed to deposit money with default currency (CHF) to an account with a different currency.@@"
            self.fail(m)
        m = "@@Incorrect balance when depositting money with default currency (CHF) to an account with a different currency.@@"
        self.assertAlmostEqual(4.589, actual, delta=0.001, msg=m)

    def test_deposit_fail_no_number(self):
        try:
            sut = BankAccount("CAD")
            sut.deposit("1.23")
        except Warning:
            pass
        except:
            m = "@@Unexpected failure when deposit amount is not a number.@@"
            self.fail(m)
        else:
            m = "@@No Warning when deposit amount is not a number.@@"
            self.fail(m)

    def test_deposit_fail_non_positive(self):
        try:
            sut = BankAccount("CAD")
            sut.deposit(-0.1)
        except Warning:
            pass
        except:
            m = "@@Unexpected failure when deposit amount is not positive.@@"
            self.fail(m)
        else:
            m = "@@No Warning when deposit amount is not positive.@@"
            self.fail(m)

    def test_withdraw(self):
        try:
            sut = BankAccount("GBP")
            sut.deposit(100.0, "GBP")
            sut.withdraw(10.0, "GBP")
            actual = sut.get_balance()
        except:
            m = "@@Failed when withdrawing GBP from a GBP account.@@"
            self.fail(m)
        m = "@@Incorrect balance after withdrawing GBP from a GBP account.@@"
        self.assertAlmostEqual(90.0, actual, delta=0.001, msg=m)

    def test_withdraw_with_explicit_conversion(self):
        try:
            sut = BankAccount("GBP")
            sut.deposit(100.0, "GBP")
            sut.withdraw(10.0, "USD")
            actual = sut.get_balance()
        except:
            m = "@@Failed when withdrawing USD from a GBP account.@@"
            self.fail(m)
        m = "@@Incorrect balance after withdrawing USD from a GBP account.@@"
        self.assertAlmostEqual(100 - 7.74, actual, delta=0.001, msg=m)

    def test_withdraw_with_implicit_conversion(self):
        try:
            sut = BankAccount("GBP")
            sut.deposit(100.0, "GBP")
            sut.withdraw(10.0)
            actual = sut.get_balance()
        except:
            m = "@@Failed when withdrawing CHF (default) from a GBP account.@@"
            self.fail(m)
        m = "@@Incorrect balance after withdrawing CHF (default) from a GBP account.@@"
        self.assertAlmostEqual(100 - 7.76, actual, delta=0.001, msg=m)

    def test_withdraw_fail_no_number(self):
        try:
            sut = BankAccount("CAD")
            sut.deposit(1000.0)
            sut.withdraw("1.23")
        except Warning:
            pass
        except:
            m = "@@Unexpected error when withdraw amount is not a number.@@"
            self.fail(m)
        else:
            m = "@@No Warning when withdraw amount is not a number.@@"
            self.fail(m)

    def test_withdraw_fail_not_positive(self):
        try:
            sut = BankAccount("CAD")
            sut.deposit(1000.0)
            sut.withdraw(-0.1)
        except Warning:
            pass
        except:
            m = "@@Unexpected error when withdraw amount is not positive.@@"
            self.fail(m)
        else:
            m = "@@No Warning when withdraw amount is not positive.@@"
            self.fail(m)

    def test_withdraw_fail_not_enough_money(self):
        try:
            sut = BankAccount("CAD")
            sut.withdraw(0.1)
        except Warning:
            pass
        except:
            m = "@@Unexpected error when withdrawing more money than available.@@"
            self.fail(m)
        else:
            m = "@@No Warning when withdrawing more money than available.@@"
            self.fail(m)

    def test_withdraw_fail_not_enough_money_with_conversion(self):
        try:
            sut = BankAccount("CHF")
            sut.deposit(10.0, "CHF")
            sut.withdraw(10.0, "EUR")
        except Warning:
            pass
        except:
            m = "@@Unexpected error when withdrawing more money than available (with conversion).@@"
            self.fail(m)
        else:
            m = "@@No Warning when withdrawing more money than available (with conversion).@@"
            self.fail(m)
