from public.item import Item
from public.order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__order_list = []

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list

    def get_order_list(self):
        if len(self.__order_list) <= 0:
            return "No order yet"
        else:
            return self.__order_list

    def set_order(self, item_list):
        new_order_list = []
        for order_item in item_list:
            if order_item in self.__menu_list:
                new_order_list.append(order_item)
        if len(new_order_list) > 0:
            new_order = Order(new_order_list)
            self.__order_list.append(new_order)

    def get_revenue(self):
        total = 0
        for order in self.__order_list:
            total = total + order.get_bill_amount()
        return total
