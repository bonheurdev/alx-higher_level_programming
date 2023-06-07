#!/usr/bin/python3
"""creates a copy of the string, removing the character at the position n"""


def remove_char_at(str, n):
    # Create a copy of the string with the character removed
    new_str = str[:n] + str[n+1:]
    if n < 0:
        return (str)
    return (new_str)
