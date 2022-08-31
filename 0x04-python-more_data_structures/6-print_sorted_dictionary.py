#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for d in sorted(list(a_dictionary)):
        print("{}: {}".format(d, a_dictionary.get(d)))
