#!/usr/bin/python3

"""This module contains ``is_same_class()`` function."""


def is_same_class(obj, a_class):
    """Checks if an `object` is an exact instance of a `class`

    Args:
        obj(object): an instance of a class
        a_class(object): a class
    """
    return type(obj) is a_class
