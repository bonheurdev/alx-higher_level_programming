#!/usr/bin/python3
"""checks for lowercase characters."""


def islower(c):
    var1 = ord(c)
    if (var1 >= 97) and (var1 <= 122):
        return True
    else:
        return False
