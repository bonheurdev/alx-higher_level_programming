#!/usr/bin/python3
""" a function that prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for keys in sorted_keys:
        val = a_dictionary[keys]
        print("{:s}: {}".format(keys, val))
