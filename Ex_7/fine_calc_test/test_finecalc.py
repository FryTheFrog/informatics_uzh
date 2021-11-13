from unittest import TestCase
from fine_calc import fine_calculator

class FineCalculatorTest(TestCase):

    def test_area_type(self): # str
        actual = fine_calculator(100, 200)
        self.assertEqual('Invalid Area Type', actual)

    def test_area_val(self): # 'urban', 'expressway', 'motorway'
        actual = fine_calculator('street', 200)
        self.assertEqual('Invalid Area Value', actual)

    def test_speed_type(self): # float/int
        actual = fine_calculator('urban', '200')
        self.assertEqual('Invalid Speed Type', actual)

    def test_speed_val(self): # positive
        actual = fine_calculator('urban', -200)
        self.assertEqual('Invalid Speed Value', actual)

    def test_legal(self): # 0
        actual = fine_calculator('urban', 50)
        self.assertEqual(0, actual)

    def test_fine_urb(self):
        self.assertEqual(400, fine_calculator('urban', 60))
    
    def test_fine_expr(self):
        self.assertEqual(320, fine_calculator('expressway', 120))
    
    def test_fine_moto(self):
        self.assertEqual(1250, fine_calculator('motorway', 180))

    def test_fine_round(self):
        self.assertEqual(35, fine_calculator('motorway', 130))