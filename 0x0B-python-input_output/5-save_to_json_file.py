#!/usr/bin/python3
"""Module that writes an object to a text file using JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Wries an object to a text file using JSON
    Args:
        my_obj (any): Object to be saved to file
        filename (str): Name of the file to save the object to
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
