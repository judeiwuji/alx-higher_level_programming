#!/usr/bin/python3

"""This module contains ``append_write()`` function."""


def append_write(filename="", text=""):
    """Appends to a file.

    Args:
        filename(string): The filename
        text(string): The content to be written
    """

    count = 0
    with open(filename, mode="a", encoding="utf-8") as fs:
        count = fs.write(text)
    return count
