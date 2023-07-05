#!/usr/bin/python3
"""a difined Rectangle class."""


class Rectangle:
    """Real definition of a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrive the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to return area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """function to return perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles based on their areas and
        return the rectangle with the larger area.
        Raises TypeError if either rect_1 or rect_2 is not
        an instance of Rectangle.
        Returns rect_1 if both have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """method to return a string representation of the object
        with any type of symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_lines = []
        for n in range(self.__height):
            rectangle_lines.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """Return a string representation of the object that
        can be used to recreate the object."""
        rect = f"Rectangle({self.__width}, {self.__height})"
        return rect

    def __del__(self):
        """called when the instance is about to be destroyed
        and removed from memory
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
