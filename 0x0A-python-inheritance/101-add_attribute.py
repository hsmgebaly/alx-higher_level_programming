#!/usr/bin/python3
"""defines a function that gives objects properties."""


def add_attribute(obj, att, value):
    """If it's possible, provide an object a new attribute.

    Arguments will be as following:
        obj (any): The object that needs an attribute added.
        att (str): the name of the attribute to be added to object.
        value (any): The att's value.
    Raises:
        TypeError: if adding the characteristic is not possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
