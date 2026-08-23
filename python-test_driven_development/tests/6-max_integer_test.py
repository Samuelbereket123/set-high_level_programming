#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max value at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test calling function with no argument passed"""
        self.assertEqual(max_integer(), None)

    def test_one_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 2.6]), 2.7)

    def test_ints_and_floats(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 5, 4.2]), 5)

    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("python"), 'y')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "zebra", "banana"]), "zebra")

    def test_negative_numbers(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_and_negative(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 0, -2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
