#!/usr/bin/python3

"""This module contains ``append_after()`` functions"""


def append_after(filename="", search_string="", new_string=""):
    """Overwrites an existing text.

    Args:
        filename(str): the file name
        search_string(str): The string to search
        new_string(str): The string to replace found string
    """
    new_text = ""
    with open(filename, encoding="utf-8") as fs:
        for line in fs:
            new_text += line
            if line.count(search_string) > 0:
                new_text += new_string
    with open(filename, encoding="utf-8", mode="w") as fs:
        fs.write(new_text)
