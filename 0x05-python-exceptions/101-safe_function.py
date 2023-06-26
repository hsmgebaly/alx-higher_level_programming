#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """For executeing a safely function .

    The arguments will be as following:
        fct: The function that should be executed.
        args: Arguments of the fct.

    Returns:
        If an error happens, then None.
        If not, the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
