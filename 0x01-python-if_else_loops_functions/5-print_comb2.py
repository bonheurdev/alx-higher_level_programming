#!/usr/bin/python3
""" prints numbers from 0 to 99 in ascending order, with two digits"""
for i in range(100):
    if i == 99:  # Check if it's the last number
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
