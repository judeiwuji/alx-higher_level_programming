#!/usr/bin/python3
import math


"""A MagicClass translated from a bytecode."""


class MagicClass:
    """MagicClass: translated from a bytecode"""

    def __init__(self, radius):
        """Creates a new MagicClass.

        Args:
            radius: (int)
        """
        self.__radius = 0

        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Computes the area using the radius"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference using the radius"""
        return 2 * math.pi * self.__radius
