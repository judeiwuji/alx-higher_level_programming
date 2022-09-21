#!/usr/bin/python3

"""This module contains LockedClass."""


class LockedClass:
    """A LockedClass."""

    def __setattr__(self, __name, __value):
        """Controls dynamic attribute setting."""
        if __name != 'first_name':
            raise AttributeError("'LockedClass' object has" +
                                 " no attribute '{}'".format(__name))
        object.__setattr__(self, __name, __value)
