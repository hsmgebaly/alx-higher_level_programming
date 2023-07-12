#!/usr/bin/python3
"""defines the MyInt class, which is an inheritor of int."""


class MyInt(int):
    """Invert the!= and == int operators."""

    def __eq__(self, value):
        """Use!= behaviour to override the == operator."""
        return self.real != value

    def __ne__(self, value):
        """Use the == behaviour to replace the!= operator."""
        return self.real == value
