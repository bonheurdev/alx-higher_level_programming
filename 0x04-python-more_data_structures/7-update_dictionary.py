#!/usr/bin/python3
"""a function that replaces or adds key/value in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    sorted_keys = sorted(a_dictionary)
    for keys in sorted_keys:
        val = a_dictionary[keys]
    return a_dictionary
