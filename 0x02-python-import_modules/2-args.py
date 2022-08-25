#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    msg = "arguments"
    if argc == 2:
        msg = "argument"

    print("{:d} {}.".format(argc - 1, msg))
    for i in range(1, argc):
        print("{:d}: {}".format(i, args[i]))
