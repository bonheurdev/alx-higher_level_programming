#!/usr/bin/python3
""" deletes the item at a specific position in a list"""


def delete_at(my_list=[], idx=0):

    if my_list:
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        else:
            x = my_list[idx]
            my_list.remove(x)
            return my_list
