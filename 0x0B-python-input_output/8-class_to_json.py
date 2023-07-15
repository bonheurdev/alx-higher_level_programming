#!/usr/bin/python3
"""For defining a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary for a simple data structure"""
    return obj.__dict__
