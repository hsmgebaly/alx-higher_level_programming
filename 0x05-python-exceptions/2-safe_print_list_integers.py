#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """For printing the 1st x elements of a list which are integers.

    Arguments will be as following:
        my_list (list): The list of items to print.
        x (int): how many items from my_list should be printed.

    Returns:
        how many printed elements there were.
    """
    retrn = 0
    for h in range(0, x):
        try:
            print("{:d}".format(my_list[h]), end="")
            retrn += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (retrn)
