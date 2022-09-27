#!/usr/bin/python3

"""This module contains ``write_file`` function."""


def write_file(filename="", text=""):
    """Writes to a file.

    Args:
        filename(string): The filename
        text(string): The content to be written
    """
    count = 0
    with open(filename, mode="w", encoding="utf-8") as fs:
        count = fs.write(text)
    return count
