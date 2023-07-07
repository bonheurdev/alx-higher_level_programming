#!/usr/bin/python3
"""adds a and b as integers.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """


def add_integer(a, b=98):
    """adds a and b as integers.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
