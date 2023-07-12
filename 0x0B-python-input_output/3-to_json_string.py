#!/usr/bin/python3
"""creates a string to JSON function definition."""
import json


def to_json_string(my_obj):
    """Give the string object's JSON representation back."""
    return json.dumps(my_obj)
