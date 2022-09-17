#!/usr/bin/python3

"""This module contains ``print_square()`` function"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size(int|float): The square size
    """

    if type(size) is not int:
        if type(size) is not float:
            raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, int(size)):
        for j in range(0, int(size)):
            print("#", end="")
        print()
