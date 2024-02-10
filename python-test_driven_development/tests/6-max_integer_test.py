#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 4]), 4)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([5, 4, 1]), 5)
        self.assertEqual(max_integer([1, 6, 2]), 6)
        self.assertEqual(max_integer([-8, 7, 8]), 8)
        self.assertEqual(max_integer([-2, -4, -3]), -2)
        self.assertEqual(max_integer([3]), 3)

    def test_value(self):
        self.assertRaises(TypeError, max_integer, ['12', 8])

    def test_float(self):
        self.assertEqual(max_integer([1.2, 3]), 3)