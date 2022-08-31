#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return [[row[x] ** 2 for x in range(len(row)) ] for row in matrix]
