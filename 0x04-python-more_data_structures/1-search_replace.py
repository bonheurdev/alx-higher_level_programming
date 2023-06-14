#!/usr/bin/python3
"""a function that use lambda replaces all
occurrences of an element by another in a new list
"""


def search_replace(my_list, search, replace):
    replaced = list(map(lambda x: replace if x == search else x, my_list))
    return replaced
