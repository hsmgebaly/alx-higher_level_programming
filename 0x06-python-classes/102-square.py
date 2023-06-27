#!/usr/bin/python3


"""Create a class Square."""


class Square:
    """Display a square."""

    def __init__(self, size=0):
        """Set-up a new square.

        The arguments will be as following:
            size (int): The new square's size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the square's current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square's current area."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the square comparison with ==."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the square comparison with != ."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the square comparison with < ."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the square comparison with <= ."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the square comparison with > ."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the square comparison with >= ."""
        return self.area() >= other.area()
