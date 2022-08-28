#!/usr/bin/python3


def max_integer(my_list=[]):
    invalid = my_list is None or len(my_list) == 0
    if invalid:
        return
    max_i = my_list[0]
    for i in my_list:
        if i > max_i:
            max_i = i
    return max_i
