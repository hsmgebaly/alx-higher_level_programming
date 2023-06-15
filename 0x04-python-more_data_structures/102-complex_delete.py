#!/usr/bin/python3
"""102-complex_delete.py"""


def complex_delete(a_dictionary, value):
    listKey = list(a_dictionary.keys())

    for valDic in listKey:
        if value == a_dictionary.get(valDic):
            del a_dictionary[valDic]

    return (a_dictionary)
