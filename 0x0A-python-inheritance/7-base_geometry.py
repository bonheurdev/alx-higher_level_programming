#!/usr/bin/python3
"""For defining an empty class BaseGeometry."""


class BaseGeometry:
    """empty base geometry class."""
    def area(self):
        """Non implemented function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str).
            value (int).
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
