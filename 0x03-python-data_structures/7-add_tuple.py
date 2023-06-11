#!/usr/bin/python3
"""Tuples addition: a function that adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 1 and len(tuple_b) >= 1:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_b[1]
        return new_tuple
    elif len(tuple_a) >= 1 and len(tuple_b) == 1:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1]
        return new_tuple
    elif len(tuple_a) >= 1 and len(tuple_b) == 0:
        new_tuple = tuple_a
        return new_tuple
    elif len(tuple_b) >= 1 and len(tuple_a) == 0:
        new_tuple = tuple_b
        return new_tuple
    else:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
