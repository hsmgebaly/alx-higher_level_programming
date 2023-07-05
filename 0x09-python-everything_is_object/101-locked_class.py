#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instant new LockedClass attributes
    for anything only the attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
