#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing Max_integer function"""
    def test_some_lists(self):
        """Tests some lists"""
        result = max_integer([0, 0, 0, 0])
        self.assertEqual(result, 0)
        result = max_integer([-1, 1, 3, 10, 10])
        self.assertEqual(result, 10)

    def test_empty_list(self):
        """Tests empty list"""
        result = max_integer()
        self.assertEqual(result, None)
    
    def test_bool_list(self):
        """Tests when an element is a boolen"""
        result = max_integer([True, 1, 2, 0])
        self.assertEqual(result, 2)
        result = max_integer([True, 0, 1])
        self.assertEqual(result, True)
        result = max_integer([1, True, 0])
        self.assertEqual(result, 1)

    def test_string_in_list(self):
        """Testing lists with strings"""
        with self.assertRaises(TypeError):
            max_integer(["Ahmad", 2, True])

    def test_one_string(self):
        """Test string"""
        result = max_integer('abc')
        self.assertEqual(result, 'c')

    def test_complex_in_list(self):
        """Testing with complex numbers"""
        with self.assertRaises(TypeError):
            max_integer([2+3j, True, 10, 2])

    def test_float_list(self):
        """Testing with floats"""
        result = max_integer([3.2, 5.9, 10.2])
        self.assertEqual(result, 10.2)

    def test_emptystring_list(self):
        """Testing with a list of empty string"""
        result = max_integer('')
        self.assertEqual(result, None)

    def test_list_one_element(self):
        """Testing with list of one element"""
        result = max_integer([1])
        self.assertEqual(result, 1)
