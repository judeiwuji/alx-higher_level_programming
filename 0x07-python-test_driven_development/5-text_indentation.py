#!/usr/bin/python3

"""This module contains `text_indentation()`"""


def text_indentation(text):
    """prints a text with 2 new lines after each \
       of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = ".\n\n".join((map(lambda d: d.strip(), text.split("."))))
    text = "?\n\n".join((map(lambda d: d.strip(), text.split("?"))))
    text = ":\n\n".join((map(lambda d: d.strip(), text.split(":"))))

    print(text, end="")
