#!/usr/bin/env python3

class ShoppingCenter:

    def __init__(self, capital, shops):
        if not shops:
            raise Warning("No shops provided")
        self.__shops = shops
        self.__capital = capital
        self.__debtors = []

    def collect_rent_and_loan(self, rent):
        for shop in self.__shops:
            amount = shop.pay_rent_and_loan(rent)
            self.__capital += amount
            if shop.get_loan() == 0 and shop in self.__debtors:
                self.__debtors.remove(shop)

    def grant_loan(self, shop, interest, amount):
        if shop in self.__shops:
            if self.__capital - amount < 0:
                raise Warning(
                    "ShoppingCenter does not have enough money to grant additional loan")
            self.__capital -= amount
            shop.take_loan(interest, amount)
            self.__debtors.append(shop)
        else:
            raise Warning("Shop is not from the shopping center")

    def add_shop(self, shop):
        self.__shops.append(shop)

    def remove_shop(self, shop):
        self.__shops.remove(shop)
        return shop

    def get_status(self):
        return (self.__capital, tuple(self.__shops), tuple(self.__debtors))

    def __len__(self):
        return len(self.__shops)
