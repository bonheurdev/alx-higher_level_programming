#!/usr/bin/python3
"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = a_dictionary.values()
    val = 0
    for value in best_score:
        if value > val:
            val = value
    for key, value in a_dictionary.items():
        if value == val:
            return key
