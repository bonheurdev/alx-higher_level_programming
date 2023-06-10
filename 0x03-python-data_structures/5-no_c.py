#!/usr/bin/python3
"""removes all characters c and C from a string"""


def no_c(my_string):
    unwanted_chars = []
    for char in my_string:
        if char.lower() != 'c':
            unwanted_chars.append(char)
    string = ''.join(unwanted_chars)
    return string
