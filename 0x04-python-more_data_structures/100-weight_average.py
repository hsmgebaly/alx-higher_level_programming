#!/usr/bin/python3
"""100-weight_average.py"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    hsm = 0

    for tuple in my_list:
        number += tuple[0] * tuple[1]
        hsm += tuple[1]

    return (number / hsm)
