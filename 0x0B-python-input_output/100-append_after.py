#!/usr/bin/python3
"""Defines the text file insertion's function."""


def append_after(filename="", search_string="", new_string=""):
    """Add the specified text after every line in
    a file that contains a particular string.

    Arguments:
        filename (str): the file's name.
        search_string (str): The target string to locate within the file.
        new_string (str): The string to add or place into the file.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
