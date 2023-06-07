#!/usr/bin/python3
"""function that prints a string in uppercase"""


def uppercase(str):
    for char in str:
        var1 = ord(char)
        if (var1 >= 97) and (var1 <= 122):      
            var2 = chr(var1 - 32)
        print("{}".format(var2), end="")
    print("")
