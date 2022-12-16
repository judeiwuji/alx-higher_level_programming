#!/usr/bin/python3
"""Module: ``find_peak`` function"""


def find_peak(list_of_integers):
    """finds the peak of the list"""
    if type(list_of_integers) is not list:
        return None

    size = len(list_of_integers)
    if size == 0:
        return None

    if size == 1:
        return list_of_integers[0]

    if list_of_integers[0] > 0 and list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[size - 1] >= list_of_integers[size - 2]:
        return list_of_integers[size - 1]

    for i in range(1, size):
        n = list_of_integers[i]
        if n >= list_of_integers[i - 1] and n >= list_of_integers[i + 1]:
            return n
