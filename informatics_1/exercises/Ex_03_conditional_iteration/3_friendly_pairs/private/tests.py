from unittest import TestCase
from public import script

def isFriendlyPair(num1, num2):
    try:
        script.num1 = num1
        script.num2 = num2 
        return script.isFriendlyPair()
    except Exception as e:
        if type(e) == TypeError:
            message = ("For the given numbers {}, {} {} is raised. Maybe you forgot to "
            "check if the given numbers are integers.").format(num1,num2,type(e).__name__)
        else :
            message = "For the given numbers {}, {} {} is raised.".format(num1,num2,type(e).__name__)
        raise type(e)(message)

class PrivateTestSuite(TestCase):

    def assertFriendly(self, num1, num2):
        try :
            actual = isFriendlyPair(num1, num2)
            expected = True
            if actual == False:
                message = "@@{} and {} are wrongly detected as not friendly pair even though they are. @@".format(num1, num2)
            else :
                message = "@@For the numbers {} and {} the function should return {}, but it returns {}.@@".format(num1, num2,repr(expected),actual)
            self.assertTrue(actual, message)  
        except Exception as e:
            self.fail(e)

    def assertNotFriendly(self, num1, num2):
        try : 
            actual = isFriendlyPair(num1, num2) 
            expected = False
            if actual == True:
                message = "@@{} and {} are wrongly detected as friendly pair even though they are not.@@".format(num1, num2,expected,actual)
            else :
                message = "@@For the numbers {} and {} the function should return {}, but it returns {}.@@".format(num1, num2,repr(expected),actual)
            self.assertFalse(actual, message)  
        except Exception as e:
            self.fail(e)

    def assertInvalid(self, num1, num2):
        try :
            actual = isFriendlyPair(num1, num2)
            expected = "Invalid"
            message = ("@@For the numbers {} and {} the function should return {} but it returns {}.@@").format(num1,num2,repr(expected),actual)
            self.assertEqual(actual, expected, message)
        except Exception as e:
            self.fail(e)

    def assertValid(self, num1, num2):
        try :
            actual = isFriendlyPair(num1, num2)
            notExpected = "Invalid"
            message = "@@For the numbers {} and {} received {} even though they are valid numbers . \
            To be valid they must be different natural numbers.@@".format(num1,num2,actual)
            self.assertNotEqual(actual, notExpected, message)
        except Exception as e:
            self.fail(e)

    def test_simple_friendlyPair(self):
        num1 = 6
        num2 = 28 
        self.assertFriendly(num1, num2)

    def test_medium_friendlyPair(self):
        num1 = 4320
        num2 = 4680  
        self.assertFriendly(num1, num2)

    def test_hard_friendlyPair(self):
        num1 = 24
        num2 = 91963648 
        self.assertFriendly(num1, num2)
    
    def test_simple_notFriendlyPair(self):
        num1 = 2
        num2 = 5
        self.assertNotFriendly(num1, num2)
    
    def test_hard_notFriendlyPair(self):
        num1 = 14326
        num2 = 4999
        self.assertNotFriendly(num1, num2)
    
    def test_invalid_sameNumbers(self):
        num1 = 20
        num2 = 20
        self.assertInvalid(num1, num2)

    def test_invalid_negative_sameNumbers(self):
        num1 = -20
        num2 = -20
        self.assertInvalid(num1, num2)     

    def test_invalid_off_point_num1(self):
        num1 = 0.99
        num2 = 28 
        self.assertInvalid(num1, num2)

    def test_valid_on_point_num1(self):
        num1 = 1
        num2 = 28
        self.assertValid(num1, num2)

    def test_invalid_off_point_num2(self):
        num1 = 6
        num2 = 0.99
        self.assertInvalid(num1, num2)

    def test_valid_on_point_num2(self):
        num1 = 28
        num2 = 1
        self.assertValid(num1, num2)

    def test_valid_out_point_num1(self):
        num1 = 28
        num2 = 2 
        self.assertValid(num1, num2)
    
    def test_invalid_float_num1(self):
        num1 = 2.6
        num2 = 28
        self.assertInvalid(num1, num2)

    def test_invalid_float_num2(self):
        num1 = 28
        num2 = 2.6
        self.assertInvalid(num1, num2)
    
    def test_invalid_float_num1_num2(self):
        num1 = 6.1
        num2 = 7.1
        self.assertInvalid(num1, num2)
