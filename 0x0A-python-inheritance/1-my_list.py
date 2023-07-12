#!/usr/bin/python3
"""the definition of the inherited list class MyList."""


class MyList(list):
    """implements sorted printing for the list class that was built-in."""

    def print_sorted(self):
        """Print an ordered list in ascending order."""
        print(sorted(self))
