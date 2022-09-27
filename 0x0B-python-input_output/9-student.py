#!/usr/bin/python3

"""This module contains ``Student`` class"""


class Student:
    """A `Student` class."""

    def __init__(self, first_name, last_name, age):
        """Creates a new student.

        Args:
            first_name(string): The student name
            last_name(string): The student last name
            age(int): The student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Serialize `Student` object."""

        obj_attrs = [d for d in dir(self) if not d.startswith("__")]
        obj_dict = {}
        for attr in obj_attrs:
            data = getattr(self, attr)
            if type(data) in (list, dict, str, int, bool):
                obj_dict[attr] = data
        return obj_dict
