#!/usr/bin/python3


def element_at(my_list, idx):
    invalid = idx < 0 or idx >= len(my_list)
    if invalid:
        return None
    return my_list[idx]
