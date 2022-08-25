#!/usr/bin/python3
import sys

if(__name__ == "__main__"):
    args = sys.argv
    argc = len(args)
    print("{} arguments.".format(argc - 1))
    
    for i in range(1, argc):
        print("{}: {}".format(i, args[i]))
