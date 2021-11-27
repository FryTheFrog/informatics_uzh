from unittest import TestCase
from onsite_restaurant import OnsiteRestaurant
from delivery_restaurant import DeliveryRestaurant
from restaurant import Restaurant

class RestaurantTest(TestCase):

    def test_restaurant_sales(self):
        r = Restaurant("Random Restaurant", "Mixed Cuisine")
        r.add_consumption_unit("Caesar Salad", 15)
        r.open_restaurant()
        r.sell_unit("Caesar Salad")
        r.sell_unit("Caesar Salad")
        self.assertEqual(30, r.get_sales())