#!/usr/bin/python3

"""This module contains `TestSquare` class."""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for `Square` class"""

    def test_sqauer(self):
        """It should create a `Square`"""

        s = Square(3)
        self.assertIsInstance(s, Square)

    def test_id(self):
        """It should create a `Square` with id == 5"""

        s = Square(3, id=5)
        self.assertEqual(s.id, 5)

    def test_properties(self):
        """It should have all properties set on creation"""

        s = Square(10, 5, 5, id=2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

    def test_no_args(self):
        """It should fail when no argument is passed during creation"""

        with self.assertRaises(TypeError):
            Square()

    def test_zero_size(self):
        """It should fail when size == 0"""

        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_size(self):
        """It should fail when size is negative"""

        with self.assertRaises(ValueError):
            Square(-10)

    def test_negative_x(self):
        """It should fail when x is negative"""

        with self.assertRaises(ValueError):
            Square(10, -2)

    def test_negative_y(self):
        """It should fail when y is negative"""

        with self.assertRaises(ValueError):
            Square(10, 5, -2)

    def test_not_int_size(self):
        """It should fail when size is not int"""

        with self.assertRaises(TypeError):
            Square("test")

    def test_not_int_x(self):
        """It should fail when x is not int"""

        with self.assertRaises(TypeError):
            Square(10, "test")

    def test_not_int_y(self):
        """It should fail when y is not int"""

        with self.assertRaises(TypeError):
            Square(10, 5, "test")

    def test_area(self):
        """It should return the area of the `Square`"""

        s = Square(10)
        self.assertEqual(s.area(), 100)

    def test_str(self):
        """It should return [Square] (1) 2/1 - 10"""

        s = Square(10, 2, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 2/1 - 10")

    def test_update_id(self):
        """It should update the id."""

        s = Square(10, 6, 2, 1)
        s.update(20)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 2)

    def test_update_size(self):
        """It should update the size."""

        s = Square(10, 6, 2, 1)
        s.update(1, 5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 2)

    def test_update_x(self):
        """It should update the x."""

        s = Square(10, 6, 2, 1)
        s.update(1, 10, 7)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 2)

    def test_update_y(self):
        """It should update the y."""

        s = Square(10, 6, 2, 1)
        s.update(1, 10, 6, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 3)

    def test_update_kw_id(self):
        """It should update the id using keyword arg."""

        s = Square(10, 6, 2, 1)
        s.update(id=20)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 2)

    def test_update_kw_size(self):
        """It should update the size using keyword arg."""

        s = Square(10, 6, 2, 1)
        s.update(id=1, size=5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 2)

    def test_update_kw_x(self):
        """It should update the x using keyword arg."""

        s = Square(10, 6, 2, 1)
        s.update(id=1, size=10, x=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)

    def test_update_kw_y(self):
        """It should update the y using keyword arg."""

        s = Square(10, 6, 2, 1)
        s.update(id=1, size=10, x=6, y=3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """It should return the dictionary representation of a Square."""

        s = Square(4, 2, 1, 10)
        s_dict = s.to_dictionary()
        test_data = {'id': 10, 'size': 4, 'x': 2, 'y': 1}
        self.assertIsInstance(s_dict, dict)
        for key in sorted(s_dict):
            self.assertEqual(s_dict[key], test_data[key])


if __name__ == "__main__":
    unittest.main()
