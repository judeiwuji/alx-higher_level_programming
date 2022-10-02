#!/usr/bin/python3

"""This module contains test cases for `Base` model."""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """`Base` test cases."""

    def test_base(self):
        """It should create a `Base` object"""

        b = Base(1)
        self.assertIsInstance(b, Base)

    def test_ids(self):
        """It should create `Base` objects with incremental ids 1, 2, 3"""
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_id_10(self):
        """It should create `Base` object with id == 10"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        """It should return the JSON string representation of list_dictionaries"""

        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        test_data = '[{"height": 7, "id": 1, "width": 10, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, test_data)

if __name__ == "__main__":
    unittest.main()
