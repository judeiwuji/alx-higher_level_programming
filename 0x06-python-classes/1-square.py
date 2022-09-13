#!/usr/bin/python3

"""This module contains the definition of a Square"""


class Square:
    """A Square class will be used to create a square shape."""

    def __init__(self, size):
        """Intantiates a square object.

        Args:
            size (int): the size of the square
        """
        self.__size = size
