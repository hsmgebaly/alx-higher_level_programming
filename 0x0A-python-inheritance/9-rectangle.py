#!/usr/bin/python3
"""defines the BaseGeometry-derived class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Apply BaseGeometry to a rectangle's representation."""

    def __init__(self, width, height):
        """Launch a new Rectangle.

        Arguments will be as following:
            width (int): the new Rectangle's width.
            height (int): the new Rectangle's height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return a Rectangle's print() and str() representation."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
