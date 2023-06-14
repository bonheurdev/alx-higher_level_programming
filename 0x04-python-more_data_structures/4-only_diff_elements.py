#!/usr/bin/python3
"""returns a set of all elements present in only one set"""


def only_diff_elements(set_1, set_2):
    diff = []
    for x in set_1:
        if x not in set_2:
            diff.append(x)
    for y in set_2:
        if y not in set_1:
            diff.append(y)
    return diff
