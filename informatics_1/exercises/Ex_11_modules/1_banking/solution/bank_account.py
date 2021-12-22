#!/usr/bin/env python3
from public.exchange_rates import EXCHANGE_RATES
from public.currency_converter import convert


class BankAccount:

    def __init__(self, currency="CHF"):
        if not currency in EXCHANGE_RATES.keys():
            raise Warning("unknown currency")
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance

    def deposit(self, amount, currency="CHF"):
        if not isinstance(amount, float) or amount <= 0:
            raise Warning("amount must be float and > 0")

        if currency != self.__currency:
            ca = convert(amount, currency, self.__currency)
        else:
            ca = amount

        self.__balance += ca

    def withdraw(self, amount, currency="CHF"):
        if not isinstance(amount, float) or amount <= 0:
            raise Warning("amount must be float and > 0")

        if currency != self.__currency:
            ca = convert(amount, currency, self.__currency)
        else:
            ca = amount

        if ca <= self.__balance:
            self.__balance -= ca
        else:
            raise Warning("insufficient funds")
