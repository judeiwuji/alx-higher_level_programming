#!/usr/bin/python3
import math

"""A MagicClass translated from a bytecode."""
class MagicClass:
    def __init__(self, radius):
        """Creates a new MagicClass.

        Args:
            radius: (int)
        """
        self.radius = 0

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """Computes the area using the radius"""
        return self.radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference using the radius"""
        return 2 * math.pi * self.radius
