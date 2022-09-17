#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test the max_integer function."""
    
    def test_max_integer(self):
        """It should return 6."""
        self.assertEqual(max_integer([2,4,6]), 6)
    
    def test_one_item(self):
        """It should return 2 when list has only one item"""
        self.assertEqual(max_integer([2]), 2)

    def test_none(self):
        """It should return None when list is empty"""
        self.assertEqual(max_integer([]), None)
