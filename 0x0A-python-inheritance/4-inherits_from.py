#!/usr/bin/python3
"""defines a class and a method for checking inherited classes."""


def inherits_from(obj, a_class):
    """Find out whether an object is a class instance
    or an inherited instance of a class.
    Arguments will be as following:
        obj (any): The object which will be checked.
        a_class (type): The class that corresponds to the obj type.
    Returns:
       True-if obj is an instance of a_class or one that has inherited from it.
        If not - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
