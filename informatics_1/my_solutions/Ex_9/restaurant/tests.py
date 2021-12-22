from unittest import TestCase
from order import Order
from restaurant import Restaurant
from item import Item

class PublicTestSuite(TestCase):
    def test_get_revenue(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        menu_list = [steak, salad, fish]
        order_list = [steak, steak, salad, pizza]
        restaurant = Restaurant("Zurich", menu_list)
        restaurant.set_order(order_list)
        actual = restaurant.get_revenue()
        expected = 60
        self.assertEqual(actual, expected)

    def test_name_menu(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        menu_list = [steak, salad, fish]
        restaurant = Restaurant("Zurich", menu_list)
        actual = restaurant.get_restaurant_name()
        expected = 'Zurich'
        self.assertEqual(actual, expected)
        actual = restaurant.get_menu_list()
        expected = [steak, salad, fish]

    def test_empty(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        menu_list = [steak, salad, fish]
        order_list = []
        restaurant = Restaurant("McDonald's", menu_list)
        restaurant.set_order(order_list)
        actual = restaurant.get_revenue()
        expected = 0
        self.assertEqual(actual, expected)
        actual = restaurant.get_order_list()
        expected = 'No order yet'
        self.assertEqual(actual, expected)

    def test_empty2(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        menu_list = [steak, salad, fish]
        order_list = [pizza, pizza]
        restaurant = Restaurant("McDonald's", menu_list)
        restaurant.set_order(order_list)
        actual = restaurant.get_revenue()
        expected = 0
        self.assertEqual(actual, expected)
        actual = restaurant.get_order_list()
        expected = 'No order yet'
        self.assertEqual(actual, expected)

    def test_multi_rest(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)

        menu_list = [steak, salad, fish]
        order_list = [steak, fish, pizza]
        restaurant = Restaurant("McDonald's", menu_list)

        menu_list2 = [steak, salad, pizza]
        order_list2 = [salad, salad, fish, pizza]
        restaurant2 = Restaurant("Burger King", menu_list2)

        restaurant.set_order(order_list)
        actual = restaurant.get_revenue()
        expected = 55
        
        restaurant2.set_order(order_list2)
        actual2 = restaurant2.get_revenue()
        expected2 = 60

        self.assertEqual(actual, expected)
        self.assertEqual(actual2, expected2)

    def test_multi_orders(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        
        menu_list = [steak, salad, fish]
        restaurant = Restaurant("McDonald's", menu_list)
        
        order_list = [steak, steak, salad]
        restaurant.set_order(order_list)
        
        order_list = [salad, fish, pizza]
        restaurant.set_order(order_list)

        order_list = []
        restaurant.set_order(order_list)

        order_list = [steak, salad, fish, fish]
        restaurant.set_order(order_list)

        actual = restaurant.get_revenue()
        expected = 195
        self.assertEqual(actual, expected)
        
        actual = restaurant.get_order_list()
        expected = [Order([steak, steak, salad]), Order([salad, fish]), Order([steak, salad, fish, fish])]
        
        self.assertEqual(str(actual), str(expected))