#!/usr/bin/python3
n = None
def magic_string():
    global n; n = 0 if n is None else n + 1
    return 'Best School' + ', Best School' * n
