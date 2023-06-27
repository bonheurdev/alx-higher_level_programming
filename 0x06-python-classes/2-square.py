#!/usr/bin/python3
"""creating an empty class Square that defines a square"""


class Square:
    """an empty class called square."""

    def __init__(self, size=0):
        """ initializing function
        Args: int(size): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
