#!/usr/bin/python3
"""creates a JSON-to-object function definition."""
import json


def from_json_string(my_str):
    """Give the JSON string's Python object representation."""
    return json.loads(my_str)
