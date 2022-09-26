#!/usr/bin/python3

"""This module contains the `BaseGeometry` class."""


class BaseGeometry:
    """The base class of all `Geometry`"""

    def area(self):
        """Computes the `area` of a `Geometry`"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates a value.

        Args:
            name(str): The `name` of the `value`
            value(int): The `value` to be stored
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creates a `Rectangle`."""

    def __init__(self, width, height):
        """Creates a `Rectangle` `instance`"""

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = int(width)
        self.__height = int(height)

    def area(self):
        """Computes the area of a `Rectangle`"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """String representation of a `Rectangle`"""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
