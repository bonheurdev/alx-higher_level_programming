#!/usr/bin/python3
"""For defining a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle class that inherit BaseGeometry."""

    def __init__(self, width, height):
        """Implement a new Rectangle.

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
