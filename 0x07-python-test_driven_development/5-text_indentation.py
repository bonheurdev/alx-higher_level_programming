#!/usr/bin/python3
"""Defines a function that indent text"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string)
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        chars_symbol = ['.', '?', ':']
        if text[i] == "\n" or text[i] in chars_symbol:
            if text[i] in chars_symbol:
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
