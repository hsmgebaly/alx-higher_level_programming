#!/usr/bin/python3
"""creates a Python class to JSON function."""


def class_to_json(obj):
    """Give the representation of
    a straightforward data structure in a dictionary."""
    return obj.__dict__
