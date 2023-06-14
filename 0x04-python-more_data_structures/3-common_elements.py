#!/usr/bin/python3
""" a function that returns a set of common elements in two sets"""


def common_elements(set_1, set_2):
    co_element = list(filter(lambda x: x in set_1 and x in set_2, set_1))
    return co_element
