#!/usr/bin/python3

"""This module contains ``to_json_string()`` function."""


import json


def to_json_string(my_obj):
    """Serialize an object to a json string.

    Args:
        obj(Object): an object.
    """

    return json.dumps(my_obj)
