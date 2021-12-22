#!/usr/bin/env python3

from public.car import Car

def assertPositiveFloat(n):
    if type(n) is not float or n < 0:
        raise Warning("Parameter not a positive float.")

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        assertPositiveFloat(gas_capacity)
        assertPositiveFloat(gas_per_100km)
        self._gas_max = gas_capacity
        self._gas_cur = gas_capacity
        self._gas_per_100km = gas_per_100km

    def fuel(self, f):
        assertPositiveFloat(f)
        if self._gas_cur + f > self._gas_max:
            raise Warning("over filling")
        self._gas_cur += f

    def get_gas_tank_status(self):
        return (self._gas_cur, self._gas_max)

    def get_remaining_range(self):
        return 100 * self._gas_cur / self._gas_per_100km

    def drive(self, dist):
        assertPositiveFloat(dist)
        dist = dist / 100
        consumption = dist * self._gas_per_100km
        if self._gas_cur < consumption:
            self._gas_cur = 0.0
            raise Warning("Gas tank is empty.")
        self._gas_cur -= consumption
