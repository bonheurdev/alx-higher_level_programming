#!/usr/bin/python3
"""a function that  prints an integer and handle exceptions"""


def safe_print_integer(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True
    except ValueError:
        return False
