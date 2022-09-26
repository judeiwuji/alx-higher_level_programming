#!/usr/bin/python3

"""This module contains the `BaseGeometry` class."""


class BaseGeometry:
    """The base class of all `Geometry`"""

    def area(self):
        """Computes the `area` of a `Geometry`"""
        raise Exception("area() is not implemented")
