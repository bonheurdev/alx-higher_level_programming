#!/usr/bin/python3
"""a function that deletes keys with a specific value in a dictionary"""


def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key, v in a_dictionary.items():
        if a_dictionary[key] == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
