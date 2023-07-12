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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
