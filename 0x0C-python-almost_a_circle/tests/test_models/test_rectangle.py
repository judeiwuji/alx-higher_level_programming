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

    def test_zero_width(self):
        """It should fail when width == 0"""

        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

    def test_zero_height(self):
        """It should fail when height == 0"""

        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)

    def test_negative_width(self):
        """It should fail when width is negative"""

        with self.assertRaises(ValueError):
            r = Rectangle(-10, 5)

    def test_negative_height(self):
        """It should fail when height is negative"""

        with self.assertRaises(ValueError):
            r = Rectangle(10, -5)

    def test_negative_x(self):
        """It should fail when x is negative"""

        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, -2)

    def test_negative_y(self):
        """It should fail when y is negative"""

        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, 2, -1)

    def test_not_int_width(self):
        """It should fail when width is not int"""

        with self.assertRaises(TypeError):
            r = Rectangle("test", 5)

    def test_not_int_height(self):
        """It should fail when height is not int"""

        with self.assertRaises(TypeError):
            r = Rectangle(10, "test")

    def test_not_int_x(self):
        """It should fail when x is not int"""

        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, "test")

    def test_not_int_y(self):
        """It should fail when y is not int"""

        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, 2, "test")

    def test_area(self):
        """It should return the area of the `Rectangle`"""

        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        """It should return [Rectangle] (12) 2/1 - 4/6"""

        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_id(self):
        """It should update the id."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_width(self):
        """It should update the width."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(10, 8)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_height(self):
        """It should update the height."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(10, 4, 8)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_x(self):
        """It should update the x."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(10, 4, 6, 7)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 1)

    def test_update_y(self):
        """It should update the y."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(10, 4, 6, 2, 6)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 6)


if __name__ == "__main__":
    unittest.main()
