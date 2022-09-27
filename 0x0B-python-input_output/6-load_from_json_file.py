#!/usr/bin/python3

"""This module contains ``load_from_json_file()`` function."""


import json


def load_from_json_file(filename):
    """Creates an object from a `JSON` file.

    Args:
        filename(str): The JSON file.
    """

    with open(filename, encoding="utf-8") as fs:
        return json.load(fs)
