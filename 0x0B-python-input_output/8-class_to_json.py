#!/usr/bin/python3

"""This module contains ``class_to_json`` function."""


def class_to_json(obj):
    """Returns a dictionary containing the attributes of an object

    Args:
        obj(object): An object
    """
    obj_attrs = [d for d in dir(obj) if not d.startswith("__")]
    obj_dict = {}
    for attr in obj_attrs:
        data = getattr(obj, attr)
        if type(data) in (list, dict, str, int, bool):
            obj_dict[attr] = data
    return obj_dict
