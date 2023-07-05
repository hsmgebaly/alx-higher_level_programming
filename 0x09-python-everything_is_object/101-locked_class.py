#!/usr/bin/python3

# establishes a locked class.


class LockedClass:
    """
    Stop the user from creating new LockedClass attributes
    for anything other than the 'first_name' attribute.
    """

    __slots__ = ["first_name"]
