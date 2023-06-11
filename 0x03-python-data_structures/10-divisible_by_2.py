#!/usr/bin/python3
"""
Return a new list with True or False, depending on whether
the integer at the same position in the original list is a multiple of 2
"""


def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for item in my_list:
            if item % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
