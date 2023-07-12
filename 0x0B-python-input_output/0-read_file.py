#!/usr/bin/python3
"""defines a function for reading text files."""


def read_file(filename=""):
    """Print a UTF8 text file's contents to the standard output."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
