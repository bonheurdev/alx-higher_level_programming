#!/usr/bin/python3
"""check if Same class or inherit from same class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Returns:
        True If obj is an instance or inherited instance of a_class.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
