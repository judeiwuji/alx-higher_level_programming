#!/usr/bin/python3

"""This module contains `TestRectangle` class."""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for `Rectangle` class"""

    def test_rectangle(self):
        """It should create a `Rectangle`"""

        r = Rectangle(10, 5)
        self.assertIsInstance(r, Rectangle)

    def test_id(self):
        """It should create a `Rectangle` with id === 5"""

        r = Rectangle(10, 5, id=5)
        self.assertEqual(r.id, 5)

    def test_properties(self):
        """It should have all properties set on creation"""

        r = Rectangle(10, 5, 5, 2, id=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 2)

    def test_no_args(self):
        """It should fail when no argument is passed during creation"""

        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_1_arg(self):
        """It should fail when only 1 argument is passed during creation"""

        with self.assertRaises(TypeError):
            r = Rectangle(5)

if __name__ == "__main__":
    unittest.main()
