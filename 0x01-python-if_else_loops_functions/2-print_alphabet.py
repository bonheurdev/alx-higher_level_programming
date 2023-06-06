#!/usr/bin/python3
"""Print the alphabet in lowercase"""
start = ord('a')
end = ord('z') + 1
for i in range(start, end):
    # convert an ASCII value back to character
    print("{}".format(chr(i)), end="")
