#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    invalid = idx < 0 or idx >= len(my_list)
    if invalid:
        return my_list
    my_list[idx] = element
    return my_list
