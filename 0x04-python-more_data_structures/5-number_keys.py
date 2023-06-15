#!/usr/bin/python3
"""5-number_keys.py"""


def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num += 1

    return (num)
