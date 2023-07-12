#!/usr/bin/python3
"""defines a function for adding files."""


def append_write(filename="", text=""):
    """adds a string to a UTF8 text file's end.

    Arguments:
        filename (str): The file's name should be entered.
        text (str): the file's text to be written.
    Returns:
        how many characters were added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
