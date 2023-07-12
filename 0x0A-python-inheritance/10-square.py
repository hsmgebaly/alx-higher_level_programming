#!/usr/bin/python3
"""defines a Square subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Display a square."""

    def __init__(self, size):
        """Launch a new square.

        Arguments will be as following:
            size (int): the new square's size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
