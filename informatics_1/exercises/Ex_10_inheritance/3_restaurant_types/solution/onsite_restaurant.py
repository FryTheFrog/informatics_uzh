#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from solution.restaurant import Restaurant


class OnsiteRestaurant(Restaurant):

    def __init__(self, name, cuisine_type, num_tables, is_open=False):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type, is_open)
        self._num_tables = num_tables
        self._available_tables = num_tables

    def occupy_table(self):
        if self._available_tables > 0:
            self._available_tables -= 1
        else:
            raise Warning()

    def free_table(self):
        if self._available_tables < self._num_tables:
            self._available_tables += 1
        else:
            raise Warning()

    def get_available_tables(self):
        return self._available_tables