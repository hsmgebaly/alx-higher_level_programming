#!/usr/bin/python3


def safe_print_integer(value):
    """For printing an integer with "{:d}".format().

    Arguments will be as following:
        value (int): The printable integer.

    Returns:
        False if a TypeError or ValueError happens.
        Otherwise, it is True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
