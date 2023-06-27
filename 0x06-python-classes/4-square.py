#!/usr/bin/python3


"""Create the class Square."""


class Square:
    """Display a square."""

    def __init__(self, size=0):
        """Set-up a new Square.

        The arguments will be as following:
            size (int): the new square's size.
        """
        self.size = size

    @property
    def size(self):
        """The square's current size can be retrieved or set."""
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
