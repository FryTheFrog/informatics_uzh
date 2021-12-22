#!/usr/bin/env python3

from public.shop import Shop


class Bakery(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__dough = 0
        self.__bread = 0

    def sell(self, price_per_unit, units):
        new_price_per_unit = price_per_unit * 0.75
        super().sell(new_price_per_unit, units)

    def produce(self, costs_per_unit):
        if self._capital < self.__dough * costs_per_unit:
            bread_produced = self._capital // costs_per_unit
            self.__bread += bread_produced
            self._capital -= bread_produced * costs_per_unit
            self.__dough -= bread_produced
            raise Warning(
                "Not enough capital to convert all the dough to bread")
        self.__bread += self.__dough
        self._capital -= self.__dough * costs_per_unit
        self.__dough = 0

    def add_procured_units(self, units):
        self.__dough += units

    def get_produced_units(self):
        return self.__bread

    def set_produced_units(self, units):
        self.__bread = units

    def pay_rent_and_loan(self, rent):
        return super().pay_rent_and_loan(round(0.8 * rent))

    def get_status(self):
        capital, loan, interest, initial_loan_amount = super().get_status()
        return (capital, loan, interest, initial_loan_amount, self.__dough,
                self.__bread)