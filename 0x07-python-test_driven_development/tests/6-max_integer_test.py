#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer       


class TestMaxInteger(unittest.TestCase):
    """Class that define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """For testing an ordered list of integers."""      
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_unordered_list(self):
        """For testing an unordered list of integers."""    
        unordered_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_begginning(self):
        """For testing a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)  

    def test_empty_list(self):
        """For testing an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """For testing a list with a single element."""     
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """For testing a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """For testing a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """For testing a single string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """For testing list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """For testing empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
