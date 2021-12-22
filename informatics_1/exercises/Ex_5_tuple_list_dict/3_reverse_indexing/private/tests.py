import os
import json
from unittest import TestCase
from unittest import TestLoader
from public import script

TestLoader.sortTestMethodsUsing = None

class PrivateTestSuite(TestCase):

    def _test_exactly(self,dataset,expected):
        try:
            actual = dict(script.reverse_index(dataset))
            message = ("@@For given dataset {} expected dictionary was {}"
                       "but the function returned {}!@@").format(dataset,expected,actual)
        except Exception as e:
            message = "An {} error is raised. Please see the details : {}".format(type(e),str(e.args))
            self.fail(message)

        self.assertDictEqual(actual,expected,message)

    def _test_roughly(self,dataset,expected):
        prefix = "For a large nested input, "
        try:
            actual = dict(script.reverse_index(dataset))
            message = "{}expected return type is dict but {} is returned!".format(prefix, type(actual).__name__)
            self.assertIsInstance(actual,dict,message)
            actual_key_len = len(actual.keys())
            expected_key_len = len(actual.keys())
            if actual_key_len != expected_key_len:
                message = (f"For a dataset containing {expected_key_len} distinct words"
                           f"in {len(dataset)} strings, your implementation returned"
                           f"a dictionary with {actual_key_len} keys.")
            elif actual.keys() != expected.keys():
                if actual.keys() - expected.keys():
                    message = (f"{prefix}found unexpected keys in resulting dictionary.")
                elif expected.keys() - actual.keys():
                    message = (f"{prefix}missing keys in resulting dictionary.")
                else:
                    # this should probably never happen?
                    message = (f"{prefix}the keys in the resulting dictionary do not match the expected keys.")
            else:
                message = (f"{prefix}the {expected_key_len} keys in the resulting dictionaries are correct, but there is something wrong with the values.")
        except Exception as e:
            message = "An {} error is raised. Please see the details : {}".format(type(e),str(e.args))
            self.fail(message)
        suffix= " On your local machine, print out the results of your function for larger input lists with many strings and compare the expected and actual results."
        message = f"@@{message}{suffix}@@"
        self.assertDictEqual(actual,expected,message)


    # Function should return empty dict if no data is provided
    def test_2_empty_dataset(self):
        dataset= []
        expected = {}
        self._test_exactly(dataset,expected)

    
    # Function should return dict type
    def test_1_return_type(self):
        actual = script.reverse_index([])
        message = "@@Expected return type is dict but {} is returned !@@".format(type(actual).__name__)
        self.assertIsInstance(actual,dict,message)
    
    # Testing with a single data dataset with 1 data 
    def test_3_single_data(self):
        dataset = ["Hello"]
        expected = {"hello":[0]}
        self._test_exactly(dataset,expected)

    # Testing with a multiple data dataset with 2 data 
    def test_4_multiple_data(self):
        dataset = ["Hello","World"]
        expected = {"hello":[0],"world":[1]}
        self._test_exactly(dataset,expected)

    # Testing case insensitivy with a multiple data dataset
    # Both should point to same index
    def test_5_case_insensitivity_1(self):
        dataset = ["Hello","hello"] 
        expected ={"hello":[0,1]}
        self._test_exactly(dataset,expected)
    
    # Testing case insensitivy with a multiple data dataset
    # Both should point to same index
    def test_5_case_insensitivity_2(self):
        dataset = ["Hello","HELLO"] 
        expected ={"hello":[0,1]}
        self._test_exactly(dataset,expected)

    # Testing single data with multiple words
    def test_6_single_data_multiple_words(self):
        dataset = ["Hello World"]
        expected ={"hello":[0],"world":[0]}
        self._test_exactly(dataset,expected) 
 
    # Testing multiple data with multiple words
    def test_7_multiple_data_multiple_words(self):
        dataset = ["Hello World","This is Info"]
        expected = {'hello': [0], 'world': [0], 'this': [1], 'is': [1], 'info': [1]}
        self._test_exactly(dataset,expected)
    
    # Testing compound words
    def test_8_compound_words(self):
        dataset = ["Hellohello","hello"]
        expected = {"hellohello":[0],"hello":[1]}
        self._test_exactly(dataset,expected)

    
    # Testing big dataset
    def test_9_big_dataset(self):
        dataset = None
        expected = None
        input_file_name = "test_data.txt"
        json_file_name = "test_expected.json"
        # Import test file
        data_file = os.path.join(os.path.dirname(__file__), input_file_name)
        json_file  = os.path.join(os.path.dirname(__file__), json_file_name)
        with open(data_file) as file:    
            dataset = file.readlines()
            dataset = [line.rstrip() for line in dataset]

        with open(json_file) as json_file:
            expected = json.load(json_file)
    
        self._test_roughly(dataset,expected)    
