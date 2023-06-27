#!/usr/bin/python3
"""creating an empty class Square that defines a square"""


class Square:
    """An empty class called square."""

    def __init__(self, size=0):
        """Initializing function
        Args: int(size): size of square
        """
        self.__size = size

    @property
    def size(self):
        """function to retrive size"""
        return self.__size

    @size.setter
    def size(self, value):
        """function to set proper value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #"""
        for i in range(0, self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print("")
