#!/usr/bin/python3

"""This module contains `matrix_divided()` function."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix(list): The matrix
        div(int): The dividsor
    """
    new_matrix = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    if type(div) is not int:
        if type(div) is not float:
            raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = None
    for row in matrix:

        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of" +
                            " lists) of integers/floats")
        if size is not None:
            if size != len(row):
                raise TypeError("Each row of the matrix must" +
                                " have the same size")
        size = len(row)
        new_row = []
        for col in row:
            if type(col) is not int:
                if type(col) is not float:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
            new_row.append(round(col/div, 2))
        new_matrix.append(new_row)
    return new_matrix
