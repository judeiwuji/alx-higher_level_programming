#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if (tuple_a is None) or (tuple_b is None):
        return None
    sum = [0, 0]
    i = 0
    for i in range(2):
        try:
            sum[i] += tuple_a[i]
            sum[i] += tuple_b[i]
        except Exception as e:
            sum[i] += 0
    return (sum[0], sum[1])
