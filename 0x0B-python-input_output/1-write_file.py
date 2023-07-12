#!/usr/bin/python3
"""defines a function for writing files."""


def write_file(filename="", text=""):
    """A UTF8 text file should include the string.

    Arguments:
        filename (str): The file's name should be entered.
        text (str): the file's text to be written.
    Returns:
        the total number of characters used.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
