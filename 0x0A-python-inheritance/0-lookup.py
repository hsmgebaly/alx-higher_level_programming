#!/usr/bin/python3
"""defines a function for looking up object attributes."""


def lookup(obj):
    """Return a list of the attributes that are available for an object."""
    return (dir(obj))
