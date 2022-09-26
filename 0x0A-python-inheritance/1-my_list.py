#!/usr/bin/python3

"""This module contains `MyList` class."""


class MyList(list):
    """This class extends built-in list"""

    def __init__(self, *args):
        """Creates an instance of a list."""

        super().__init__(args)

    def print_sorted(self):
        """prints sorted list"""
        print("[", end="")
        for i, e in enumerate(sorted(self)):
            if i > 0:
                print(end=", ")
            print("{:d}".format(e), end="")
        print("]")
