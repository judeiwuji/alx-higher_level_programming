#!/usr/bin/python3

"""This module contains ``pascal_triangle()`` function."""


def factorial(n):
    result = 1

    for i in range(n, 1, -1):
        result *= i
    return result


def ncr(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))


def pascal_triangle(n):
    """Pascals triangle.

    Args:
        n(int): The length of the list
    """
    triangle = []

    if n <= 0:
        return triangle

    i = 0
    while i < n:
        row = []
        j = 0
        while j <= i:
            row.append(int(ncr(i, j)))
            j += 1
        triangle.append(row)
        i += 1
    return triangle
