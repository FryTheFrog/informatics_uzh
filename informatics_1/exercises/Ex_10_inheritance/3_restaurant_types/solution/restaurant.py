#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
import copy

class Restaurant:

    def __init__(self, name, cuisine_type, is_open = False):
        self._name = name
        self._cuisine_type = cuisine_type
        self._sales = 0
        self._is_open = is_open
        self._consumption_units = {}

    def describe_restaurant(self):
        return self._name + " provides amazing " + self._cuisine_type

    def open_restaurant(self):
        self._is_open = True

    def close_restaurant(self):
        self._is_open = False

    def is_open(self):
        return self._is_open

    def add_consumption_unit(self, name, price):
        self._consumption_units[name] = price

    def remove_consumption_unit(self, name):
        del self._consumption_units[name]

    def get_menu(self):
        return copy.deepcopy(self._consumption_units)

    def sell_unit(self, name):
        if self._is_open:
            self._sales += self._consumption_units[name]
        else:
            raise Warning()

    def get_sales(self):
        return self._sales

