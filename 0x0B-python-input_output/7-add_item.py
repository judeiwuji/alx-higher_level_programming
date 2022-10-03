#!/usr/bin/python3

"""This module contains ``load_from_json_file()`` function."""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """adds all arguments to a Python list, and then save them to a file:"""
    a_list = []

    for i in range(1, len(sys.argv)):
        a_list.append(sys.argv[i])
    try:
        data = load_from_json_file("add_item.json")
        if type(data) is list:
            data.extend(a_list)
            a_list = data
    except FileNotFoundError:
        pass
    save_to_json_file(a_list, "add_item.json")


if __name__ == "__main__":
    main()
