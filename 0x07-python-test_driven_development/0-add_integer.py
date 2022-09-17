#!/usr/bin/python3

""""
This module contains `add_integer` function

USAGE:
>>> add_integer(2,3)
5
"""


def add_integer(a, b=98):
    """adds 2 integers

    Args:
        a(int|float): first number
        b(int|float): second number
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
    return int(a) + int(b)
