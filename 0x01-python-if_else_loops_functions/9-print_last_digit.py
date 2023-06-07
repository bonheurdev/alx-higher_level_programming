#!/usr/bin/python3
"""function that prints the last digit of a number."""


def print_last_digit(number):
    print(abs(number) % 10, end="")
    the_value = abs(number) % 10
    return the_value
