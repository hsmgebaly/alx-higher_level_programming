#!/usr/bin/python3


"""Create the class Square."""


class Square:
    """Display a square."""

    def __init__(self, size=0):
        """Set-up a new Square.

        The arguments will be as following:
            size (int): the new square's size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
