#!/usr/bin/python3
"""a function that  prints an integer and handle exceptions"""


def safe_print_integer(value):
    try:
        int_value = value
        print("{:d}".format(int_value))
        return True
    except (TypeError, ValueError):
        return False
