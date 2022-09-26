#!/usr/bin/python3

"""This module contains the `lookup()` function."""


def lookup(obj):
    """Returns all attributes of an object.

    Args:
        obj(Any): The object
    """
    if obj is None:
        return []
    return dir(obj)
