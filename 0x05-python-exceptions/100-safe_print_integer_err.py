#!/usr/bin/python3
import sys
""" a function that prints an integer"""


def safe_print_integer_err(value):
    try:
        int_value = value
        print("{:d}".format(int_value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
