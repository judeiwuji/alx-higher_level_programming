#!/usr/bin/python3

"""This module contains `MyInt` class."""


class MyInt(int):
    """Creates an integer"""

    def __eq__(self, other):
        """inverts equality check"""

        return super().__ne__(other)

    def __ne__(self, other) -> bool:
        """inverts unequality check"""

        return super().__eq__(other)
