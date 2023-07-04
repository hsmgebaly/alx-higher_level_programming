#!/usr/bin/python3
# finding the largest integer in a list module

def max_integer(list=[]):
    """ Function to locate and return the largest number in a list of numbers
        The function returns None if the list contains no items.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
