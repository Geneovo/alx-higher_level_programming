#!/usr/bin/python3
"""Modules that defines a function to add a new attribute to an object"""


def add_attributes(obj, attr, value):
    """Adds a new attributes to an object if possible
    Args:
        obj (any): The object to add an attributes to
        att (str): The name of the attribute to add to obj
        value (any): The value of att
    Raises:
        TypeError: if the attributes cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
