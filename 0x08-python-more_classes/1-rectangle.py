#!/usr/bin/python3
#defines a class for rectangles.


class Rectangle:
#Create a rectangle.

    def __init__(self, width=0, height=0):
        """Init a new Rectangle From scratch.

        Arguments will be as following:
            width (int): the new rectangle's width.
            height (int): the new rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
