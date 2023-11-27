#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test methods"""
    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered(self):
        unordered = [5, 67, 32, -1]
        self.assertEqual(max_integer(unordered), 67)

    def test_with_floats(self):
        floated = [2.3, 4.0, 54.6, 1.9]
        self.assertEqual(max_integer(floated), 54.6)

    def test_with_strings(self):
        val = "string"
        self.assertEqual(max_integer(val), 't')

    def test_string_list(self):
        a_list = ["hello", "world", "welcome"]
        self.assertEqual(max_integer(a_list), "world")

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

    def test_mixed_list(self):
        mixed = [2, 4.5, -2, -89.0]
        self.assertEqual(max_integer(mixed), 4.5)

    def test_list_with_one_element(self):
        lists = [5]
        self.assertEqual(max_integer(lists), 5)


if __name__ == '__main__':
    unittest.main()
