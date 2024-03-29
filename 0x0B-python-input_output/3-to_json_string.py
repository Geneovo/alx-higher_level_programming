#!/usr/bin/python3
"""Module that returns the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj (any): Object to be converted to JSON
    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
