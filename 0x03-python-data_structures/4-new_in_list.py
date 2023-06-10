#!/usr/bin/python3
"""
replaces an element in a list at a specific
position without modifying the original list
"""


def new_in_list(my_list, idx, element):
    length = len(my_list)
    copy = my_list.copy()
    if idx < 0:
        return copy
    elif idx >= length:
        return copy
    else:
        copy[idx] = element
        return copy
