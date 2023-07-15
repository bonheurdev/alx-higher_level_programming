#!/usr/bin/python3
"""For defining a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return Python object representation of a JSON string."""
    return json.loads(my_str)
