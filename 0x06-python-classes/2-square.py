#!/usr/bin/python3

"""This module contains the definition of a Square"""


class Square:
    """A Square class will be used to create a square shape."""

    def __init__(self, size=0):
        """Intantiates a square object.

        Args:
            size (int): the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
