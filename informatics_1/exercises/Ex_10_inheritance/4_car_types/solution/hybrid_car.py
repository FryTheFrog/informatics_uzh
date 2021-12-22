#!/usr/bin/env python3

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar

def assertPositiveFloat(n):
    if type(n) is not float or n < 0:
        raise Warning("Parameter not a positive float.")

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self._use_battery = True

    def switch_to_combustion(self):
        self._use_battery = False

    def switch_to_electric(self):
        self._use_battery = True

    def get_remaining_range(self):
        c = CombustionCar.get_remaining_range(self)
        e = ElectricCar.get_remaining_range(self)
        return c+e

    def drive(self, dist):
        assertPositiveFloat(dist)
        if dist > self.get_remaining_range():
            self._gas_cur = 0
            self._battery_cur = 0
            raise Warning("Distance is too far, even with tank+battery combined!")
        if self._use_battery:
            e = ElectricCar.get_remaining_range(self)
            if dist > e:
                ElectricCar.drive(self, e)
                self.switch_to_combustion()
                CombustionCar.drive(self, dist - e)
            else:
                ElectricCar.drive(self, dist)
        else:
            c = CombustionCar.get_remaining_range(self)
            if dist > c:
                CombustionCar.drive(self, c)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - c)
            else:
                CombustionCar.drive(self, dist)
