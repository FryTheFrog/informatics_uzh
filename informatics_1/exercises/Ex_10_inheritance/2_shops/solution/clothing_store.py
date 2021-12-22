#!/usr/bin/env python3

from public.shop import Shop


class ClothingStore(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__clothing_pieces = 0

    def procure(self, price_per_unit, units):
        price_paid = price_per_unit
        if units > 10:
            price_paid = 0.8 * price_per_unit
        super().procure(price_paid, units)

    def add_procured_units(self, units):
        self.__clothing_pieces += units

    def get_produced_units(self):
        return self.__clothing_pieces

    def set_produced_units(self, units):
        self.__clothing_pieces = units

    def get_status(self):
        capital, loan, interest, initial_loan_amount = super().get_status()
        return (
        capital, loan, interest, initial_loan_amount, self.__clothing_pieces)