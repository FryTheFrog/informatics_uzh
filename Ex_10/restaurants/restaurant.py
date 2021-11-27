import copy


class Restaurant:

    def __init__(self, name, cuisine_type, is_open=False):
        self.__name = name
        self.__cuisine_type = cuisine_type
        self.__is_open = is_open
        self.__menu = dict()
        self.__sales = 0

    def describe_restaurant(self):
        return f"{self.__name}: {self.__cuisine_type}"

    def open_restaurant(self):
        self.__is_open = True

    def close_restaurant(self):
        self.__is_open = False

    def is_open(self):
        return self.__is_open

    def add_consumption_unit(self, name, price):
        self.__menu[name] = price

    def remove_consumption_unit(self, name):
        del self.__menu[name]

    def get_menu(self):
        return copy.deepcopy(self.__menu)

    def sell_unit(self, name):
        if self.__is_open:
            self.__sales += self.__menu[name]
        else: raise Warning('restaurant is closed')

    def get_sales(self):
        return self.__sales