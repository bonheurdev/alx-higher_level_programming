#!/usr/bin/python3
"""Print all the letters except q and e"""
start = ord('a')
end = ord('z') + 1
for i in range(start, end):
    char = chr(i)
    if char != 'e' and char != 'q':
        print("{}".format(char), end="")
