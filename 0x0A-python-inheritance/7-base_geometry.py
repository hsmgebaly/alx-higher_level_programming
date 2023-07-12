#!/usr/bin/python3
"""defines a base geometry class called BaseGeometry."""


class BaseGeometry:
    """Display base geometry."""

    def area(self):
        """No implementation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verify an input parameter's integer status.

        Arguments will be as following:
            name (str): the parameter's name.
            value (int): the criteria to be verified.
        Raises:
            TypeError: when value is not an integer.
            ValueError: If value is greater than zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
