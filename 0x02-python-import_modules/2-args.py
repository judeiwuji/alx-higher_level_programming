#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    msg = "arguments"
    if argc <= 1:
        msg = "argument"

    print("{} {}.".format(argc - 1, msg))
    for i in range(1, argc):
        print("{}: {}".format(i, args[i]))
