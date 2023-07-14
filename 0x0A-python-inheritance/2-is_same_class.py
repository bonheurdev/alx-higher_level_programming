#!/usr/bin/python3
"""checkking for Exact same object"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of specified class.

    Returns:
        True If obj is exactly an instance of a_class.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
