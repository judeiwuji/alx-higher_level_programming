#!/usr/bin/python3

"""This module contains `lazy_matrix_mul()`"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Computes the products of 2 matrices"""
    a = np.array(m_a)
    b = np.array(m_b)
    return np.matmul(a, b)
