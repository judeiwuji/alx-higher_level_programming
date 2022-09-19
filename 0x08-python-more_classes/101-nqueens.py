#!/usr/bin/python3

"""This module solves the N queens puzzle."""

import sys


def isdigit(n):
    """checks if a str is a digit"""
    for c in n:
        if not (ord(c) >= 48 and ord(c) <= 57):
            return False
    return True


def main():
    """Program entry point"""
    argc = len(sys.argv)

    if argc != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    if not isdigit(N):
        print("N must be a number")
        sys.exit(1)

    n = int(N)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    chess = [[col for col in range(0, n)] for row in range(0, n)]


if __name__ == "__main__":
    main()
