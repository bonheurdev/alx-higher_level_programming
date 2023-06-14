#!/usr/bin/python3
"""a function that adds all unique integers in a list
    (only once for each integer).
"""


def uniq_add(my_list=[]):
    unique_set = set(my_list)  # Convert the list to a set to remove duplicates
    result = sum(unique_set)  # Calculate the sum of the unique integers
    return result
