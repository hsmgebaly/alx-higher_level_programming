#!/usr/bin/python3


"""Create a MagicClass that exactly matches a bytecode
	that Holberton has provided."""

import math


class MagicClass:
    """Display a circle."""

    def __init__(self, radius=0):
        """Set-up a MagicClass.

        The arguments will be as following:
            radius (float or int): The new MagicClass's radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the MagicClass's area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the MagicClass's circumference."""
        return (2 * math.pi * self.__radius)
