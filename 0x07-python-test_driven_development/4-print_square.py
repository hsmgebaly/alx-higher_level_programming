#!/usr/bin/python3
# Defines a square-printing function.

def print_square(size):
    """ Print the # symbol in the shape of a square.

    Arguments will be as  following:
        size (int): The square’s height/width.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
