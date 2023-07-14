#!/usr/bin/python3
"""for defining  a class MyList that inherits from list."""


class MyList(list):
    """Implements MyList class that inherits from list."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
