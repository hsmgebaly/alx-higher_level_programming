#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 1 and ord(char) <= 26:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
