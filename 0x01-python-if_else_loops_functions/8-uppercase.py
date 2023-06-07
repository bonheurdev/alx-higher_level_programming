#!/usr/bin/python3
"""function that prints a string in uppercase"""


def uppercase(str):
    for charac in str:
        # use charac
        if ord(charac) >= 97 and ord(charac) <= 122:
            charac = chr(ord(charac) - 32)
        print("{}".format(charac), end="")        
    print("")
