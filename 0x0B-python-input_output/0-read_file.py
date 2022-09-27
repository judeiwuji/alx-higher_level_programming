#!/usr/bin/python3

"""This module contains ``read_file()`` function"""


def read_file(filename=""):
    """Reads the content of a file."""

    with open(filename, encoding="utf-8") as fs:
        for line in fs:
            print(line, end="")
