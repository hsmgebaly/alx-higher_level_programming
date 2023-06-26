#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """For printing x elememts of the list

    Arguments will be as following:
        my_list (list): The list of items to print.
        x (int): how many items from my_list should be printed.

    Returns:
       Print how many printed elements there were.
    """
    retrn = 0
    for h in range(x):
        try:
            print("{}".format(my_list[h]), end="")
            retrn += 1
        except IndexError:
            break
    print("")
    return (retrn)
