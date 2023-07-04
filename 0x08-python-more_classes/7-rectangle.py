#!/usr/bin/python3
#Defines a class for Rectangle.


class Rectangle:
    """Create a rectangle.

    Attr as following:
        number_of_instances (int): How many Rectangle instances there are.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
	"""Init a new Rectangle from scratch.

        Arguments will be as following:
            width (int): the new rectangle's width.
            height (int): the new rectangle's height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
#Get/set the Rectangle's width.
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
#Get/set the Rectangle's height.
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
#Return the Rectangle's area.
        return (self.__width * self.__height)

    def perimeter(self):
#Return the Rectangle's perimeter.
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
	"""Return the Rectangle's printable representation.

	uses the character # to symbolise the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
#Return the Rectangle's string representation.
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
#For each Rectangle that is deleted, print a message.
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
