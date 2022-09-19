#!/usr/bin/python3

"""This module contains ``matrix_mul()`` function."""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    size = None
    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if size is not None:
            if size != len(row_a):
                raise TypeError("each row of m_a must be of the same size")
            if len(row_a) != len(m_b):
                raise ValueError("m_a and m_b can't be multiplied")
        size = len(row_a)

    size = None
    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if size is not None:
            if size != len(row_b):
                raise TypeError("each row of m_b must be of the same size")
        size = len(row_b)
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    m_c = []
    for i in range(0, len(m_a)):
        prod = []
        for j in range(0, len(m_a[i])):
            result = 0
            for m in range(0, len(m_b)):
                if type(m_a[i][m]) is not int:
                    if type(m_a[i][m]) is not float:
                        raise TypeError("m_a should contain only" +
                                        " integers or floats")
                if type(m_b[m][j]) is not int:
                    if type(m_b[m][j]) is not float:
                        raise TypeError("m_b should contain" +
                                        " only integers or floats")
                result += m_a[i][m] * m_b[m][j]
            prod.append(result)
        m_c.append(prod)
    return m_c
