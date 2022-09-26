#!/usr/bin/python3

"""This module contains `` function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited \
        (directly or indirectly) from the specified class
    Args:
        obj(object): The object
        a_class(object): Class to be checked
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
