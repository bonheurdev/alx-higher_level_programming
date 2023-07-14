#!/usr/bin/python3
"""checks if sub class of a class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Returns:
        True if obj is an inherited instance of a_class
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
