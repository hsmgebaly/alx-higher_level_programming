#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """For printing an integer with "{:d}".format().

    A related message is displayed to standard error
	if a ValueError message is recognised.

    The arguments will be as following:
        value (int): a printable integer.

    Returns:
        False if a TypeError or ValueError happens.
        Otherwise, it is True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
