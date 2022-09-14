#!/usr/bin/python3
import math

"""This module contains a class translated from a bytecode"""
class MagicClass:
    """MagicClass is translated from a bytecodes"""
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
