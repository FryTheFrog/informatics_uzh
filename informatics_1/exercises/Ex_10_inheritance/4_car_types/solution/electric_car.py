#!/usr/bin/env python3

from public.car import Car

def assertPositiveFloat(n):
    if type(n) is not float or n < 0:
        raise Warning("Parameter not a positive float.")

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        assertPositiveFloat(battery_size)
        assertPositiveFloat(battery_range_km)
        self._battery_cur = battery_size
        self._battery_max = battery_size
        self._range = battery_range_km

    def charge(self, kwh):
        assertPositiveFloat(kwh)
        if kwh + self._battery_cur > self._battery_max:
            raise Warning("Overcharge")
        self._battery_cur += kwh

    def get_battery_status(self):
        return (self._battery_cur, self._battery_max)

    def get_remaining_range(self):
        return self._battery_cur / self._consumption_per_km()

    def drive(self, dist):
        assertPositiveFloat(dist)
        consumption = dist * self._consumption_per_km()
        if consumption > self._battery_cur:
            self._battery_cur = 0.0
            raise Warning("Battery depleted.")
        self._battery_cur -= consumption

    def _consumption_per_km(self):
        return self._battery_max / self._range
