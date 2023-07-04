#!/usr/bin/python3
"""6-max_integer_test.py"""
# Unittests for max_integer([..]).

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
# Max_integer([..]) unit tests should be defined.

    def test_ordered_list(self):
# Check the integers in an ordered list.
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
# Check the integers in an unordered list.
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
# Test a list with a maximum value at the start.
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
# Test using a blank list.
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
# Examine a list with just one element.
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
# Test a collection of floats.
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
# Test a collection of floats and ints.
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
# Check the string.
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
# Check the list of string.
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
# Check the empty string.
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
