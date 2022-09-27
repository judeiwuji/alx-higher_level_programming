#!/usr/bin/python3

"""This module contains ``from_json_string()`` function."""


import json
from io import StringIO


def from_json_string(my_str):
    """"Deserialize JSON string to python object.

    Args:
        my_str(string): JSON doc.
    """

    return json.load(StringIO(my_str))
