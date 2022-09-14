#!/usr/bin/python3

"""This module contains a class translated from a bytecode"""

import math


class MagicClass:
    """Translated from a bytecode"""
    def __init__(self, radius=None):
        """Instantiate a new object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Computes the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference"""
        return 2 * math.pi * self.__radius
