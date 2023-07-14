#!/usr/bin/python3
"""For defining a class  that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """invert by Overriding == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """invert by Overriding != operator with == behavior."""
        return self.real == value
