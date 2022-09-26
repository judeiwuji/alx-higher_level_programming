#!/usr/bin/python3

"""This module contains ``is_kind_of_class()`` function."""


def is_kind_of_class(obj, a_class):
    """Checks if an `object` is an instance of a `class`

    Args:
        obj(object): an instance of a class
        a_class(object): a class
    """
    return isinstance(obj, a_class)
