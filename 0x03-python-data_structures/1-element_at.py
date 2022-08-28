#!/usr/bin/python3


def element_at(my_list, idx):
    invalid = idx < 0 or len(my_list) < idx
    if invalid:
        return None
    return my_list[idx]
    