#!/usr/bin/python3

"""This module contains ``add_attribute()`` function"""


class ContextManager():
    """Context manager class."""

    def __init__(self):
        """Create a context."""
        pass

    def __enter__(self):
        """Enter a context"""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exits from a context"""
        return True


def add_attribute(mc, name, value):
    """Add an attribute to an object.

    Args:
        name(str): The name of the value
        value(Any): The value to be set
    """
    with ContextManager() as manager:
        setattr(mc, name, value)
    if hasattr(mc, name) is False:
        raise TypeError("can't add new attribute")
