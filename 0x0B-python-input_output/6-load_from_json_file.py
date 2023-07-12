#!/usr/bin/python3
"""defines a function for reading JSON files."""
import json


def load_from_json_file(filename):
    """From a JSON source, create a Python object."""
    with open(filename) as f:
        return json.load(f)
