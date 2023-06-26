#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """element by element divides two lists.

    Arguments will be as following:
        my_list_1 (list): 1st list.
        my_list_2 (list): 2nd list.
        list_length (int): How many number of elemnts will be divided

    Returns:
        a new list with the length list_length that includes each division.
    """
    new_list = []
    for h in range(0, list_length):
        try:
            div = my_list_1[h] / my_list_2[h]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
