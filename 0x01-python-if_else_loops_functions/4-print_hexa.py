#!/usr/bin/python3
"""prints all numbers from 0 to 98 in decimal and in hexadecimal"""
for i in range(99):
    var = '0x'  # variable to store 0x
    print('{} = {}{:x}'.format(i, var, i))
