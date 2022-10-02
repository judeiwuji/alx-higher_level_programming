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

    def test_update_kw_id(self):
        """It should update the id using keyword arg."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(id=20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_kw_width(self):
        """It should update the width using keyword arg."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(id=10, width=8)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_kw_height(self):
        """It should update the height using keyword arg."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(id=10, width=4, height=8)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_kw_x(self):
        """It should update the x using keyword arg."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(id=10, width=4, height=6, x=7)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 1)

    def test_update_kw_y(self):
        """It should update the y using keyword arg."""

        r = Rectangle(4, 6, 2, 1, 10)
        r.update(id=10, width=4, height=6, x=2, y=6)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        """It should return the dictionary representation of a Rectangle."""

        r = Rectangle(4, 6, 2, 1, 10)
        r_dict = r.to_dictionary()
        test_data = {'height': 6, 'id': 10, 'x': 2, 'y': 1, 'width': 4}
        self.assertIsInstance(r_dict, dict)
        for key in sorted(r_dict):
            self.assertEqual(r_dict[key], test_data[key])

    def test_to_json_string(self):
        """It should return the JSON string representation of list_dictionaries"""

        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(20, 10, 5, 8, 2)
        dictionary1 = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary1, dictionary2])
        test_data = '[{"height": 7, "id": 1, "width": 10, "x": 2, "y": 8}, ' + \
                    '{"height": 10, "id": 2, "width": 20, "x": 5, "y": 8}]'
        self.assertEqual(json_dictionary, test_data)

    def test_save_to_file(self):
        """It should write the JSON string representation of list_objs to a file"""

        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        rect_list = Rectangle.load_from_file()
        self.assertIsInstance(rect_list[0], Rectangle)

    def test_from_json_string(self):
        """It should return the list of the JSON string representation json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        list_dict = Rectangle.from_json_string(json_dictionary)
        self.assertIsInstance(list_dict, list)

    def test_create(self):
        """It should return an instance with all attributes already set"""

        r = Rectangle.create(width=10, height=5, x=2, y=1, id=100)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)


if __name__ == "__main__":
    unittest.main()
