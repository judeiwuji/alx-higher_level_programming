#!/usr/bin/python3

"""This module contains ``save_to_json_file`` function."""


import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a file in `JSON` format.

    Args:
        my_obj(object): The object to be `serialize`
        filename(str): The file to store the `JSON`
    """

    with open(filename, mode="w", encoding="utf-8") as fs:
        json_data = json.dumps(my_obj)
        fs.write(json_data)
