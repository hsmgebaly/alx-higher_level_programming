#!/usr/bin/python3
"""defines a function for class checking."""


def is_same_class(obj, a_class):
    """Verify if an object is a precise instance of the specified class.

    Arguments will be as following:
        obj (any): The object which will be checked.
        a_class (type): a class that corresponds to the object's kind.
    Returns:
        True - if obj precisely matches an instance of a_class.
        If not - False.
    """
    if type(obj) == a_class:
        return True
    return False
