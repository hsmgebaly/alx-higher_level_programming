#!/usr/bin/python3


"""Create a class Square."""


class Square:
    """Display a square."""

    def __init__(self, size):
        """Set-up a new square.

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

    def my_print(self):
        """Print the # symbol in the square."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
