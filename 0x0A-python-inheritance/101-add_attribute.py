#!/usr/bin/python3

"""This module contains ``add_attribute()`` function"""


from contextlib import suppress


def add_attribute(mc, name, value):
    """Add an attribute to an object.
    
    Args:
        name(str): The name of the value
        value(Any): The value to be set
    """
    with suppress(AttributeError):
        setattr(mc, name, value)
    if hasattr(mc, name) == False:
        raise TypeError("can't add new attribute")
    
