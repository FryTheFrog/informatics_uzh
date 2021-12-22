#!/usr/bin/env python3
from unittest import TestCase
from public.exchange_rates import EXCHANGE_RATES
from public.currency_converter import convert


class PrivateCurrencyConverterTest(TestCase):

    def _assert_exchange_rates(self):
        expected = {
            "CAD": {
                "USD": 0.753,
                "JPY": 82.463,
                "EUR": 0.684,
                "GBP": 0.583
            },
            "CHF" : {
                "USD": 1.001,
                "GBP": 0.776,
                "CAD": 1.330
            },
            "EUR": {
                "CHF": 1.100,
                "GBP": 0.853
            },
            "USD": {
                "EUR": 0.908,
                "GBP": 0.774,
                "JPY": 109.510
            },
            "GBP": {},
            "JPY": {
                "GBP": 0.707,
                "EUR": 0.829,
                "CHF": 0.912
            }
        }
        m = "@@The dictionary of exchange rates has been changed.@@"
        self.assertEqual(expected, EXCHANGE_RATES, m)

    def test_0_exchange_rates(self):
        self._assert_exchange_rates()

    def test_1a_convert_direct(self):
        self._assert_exchange_rates()
        try:
            actual = convert(1.0, "USD", "GBP")
            expected = 0.774
        except:
            m = "@@Failed to convert an amount from USD to GBP.@@"
            self.fail(m)
        m = "@@Incorrect results when converting an amount from USD to GBP.@@"
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    def test_1b_convert_indirect(self):
        self._assert_exchange_rates()
        try:
            actual = convert(1.0, "EUR", "CAD")
            expected = 1/0.684
        except:
            m = "@@Failed to convert an amount from EUR to CAD.@@"
            self.fail(m)
        m = "@@Incorrect results when converting an amount from EUR to CAD.@@"
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    def test_1c_convert_non_existing_first(self):
        self._assert_exchange_rates()
        try:
            convert(1.0, "EUR", "RUB")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when source currency does not exist.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when source currency does not exist.@@"
            self.fail(m)

    def test_1c_convert_non_existing_second(self):
        self._assert_exchange_rates()
        try:
            convert(1.0, "RUB", "EUR")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when target currency does not exist.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when target currency does not exist.@@"
            self.fail(m)

    def test_2a_convert_direct_actual_amount(self):
        self._assert_exchange_rates()
        try:
            actual = convert(123.45, "USD", "GBP")
            expected = 123.45 * 0.774
        except:
            m = "@@Failed to convert an amount from USD to GBP.@@"
            self.fail(m)
        m = "@@Incorrect results when converting an amount from USD to GBP.@@"
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    def test_2b_convert_indirect_actual_amount(self):
        self._assert_exchange_rates()
        try:
            actual = convert(234.56, "EUR", "CAD")
            expected = 234.56 / 0.684
        except:
            m = "@@Failed to convert an amount from EUR to CAD.@@"
            self.fail(m)
        m = "@@Incorrect results when converting an amount from EUR to CAD.@@"
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    def test_2c_convert_non_existing_actual_amount_first(self):
        self._assert_exchange_rates()
        try:
            convert(567.89, "RUB", "EUR")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when source currency does not exist.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when source currency does not exist.@@"
            self.fail(m)

    def test_2c_convert_non_existing_actual_amount_second(self):
        self._assert_exchange_rates()
        try:
            convert(456.78, "EUR", "RUB")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when target currency does not exist.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when target currency does not exist.@@"
            self.fail(m)

    def test_3a_fail_no_number(self):
        self._assert_exchange_rates()
        try:
            convert("1.234", "EUR", "RUB")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when amount is not a number.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when amount is not a number.@@"
            self.fail(m)

    def test_3b_fail_invalid_from_currency_a(self):
        self._assert_exchange_rates()
        try:
            convert(1.23, 1, "EUR")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when source currency is invalid.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when source currency is invalid.@@"
            self.fail(m)

    def test_3b_fail_invalid_from_currency_b(self):
        self._assert_exchange_rates()
        try:
            convert(1.23, "", "EUR")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when source currency is invalid.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when source currency is invalid.@@"
            self.fail(m)

    def test_3c_fail_invalid_to_currency_a(self):
        self._assert_exchange_rates()
        try:
            convert(1.23, "EUR", 1)
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when target currency is invalid.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when target currency is invalid.@@"
            self.fail(m)

    def test_3c_fail_invalid_to_currency_b(self):
        self._assert_exchange_rates()
        try:
            convert(1.23, "EUR", "")
        except Warning:
            pass
        except:
            m = "@@Currency conversion failed with an unexpected error when target currency is invalid.@@"
            self.fail(m)
        else:
            m = "@@Currency conversion does not fail when target currency is invalid.@@"
            self.fail(m)
