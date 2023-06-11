#!/usr/bin/python3
""" deletes the item at a specific position in a list"""


def delete_at(my_list=[], idx=0):
    # check If idx is negative or out of range, return no change
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
    return my_list
