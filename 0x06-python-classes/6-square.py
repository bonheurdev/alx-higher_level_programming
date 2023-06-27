#!/usr/bin/python3
"""creating an empty class Square that defines a square"""


class Square:
    """An empty class called square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing function
        Args: int(size): size of square
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """function to retrive position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Function to set the proper value of position"""
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                any(not isinstance(num, int) or num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character '#' respecting the position."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
