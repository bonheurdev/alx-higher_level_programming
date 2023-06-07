#!/usr/bin/python3

def uppercase(str):
    """function that prints a string in uppercase."""

    for char in str:
        # use char
        if ord(char) >= 97 and ord(char) <= 122:     
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    else:
        print("")
