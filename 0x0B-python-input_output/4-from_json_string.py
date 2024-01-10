#!/usr/bin/python3
"""Module that returns an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str (str): JSON string to be converted to an object
    Returns:
        any: Python data structure representing the object
    """
    return json.loads(my_str)
