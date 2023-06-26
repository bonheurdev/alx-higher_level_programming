#!/usr/bin/python3
import sys
"""a function that executes a function
and handle exceptions safely
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
