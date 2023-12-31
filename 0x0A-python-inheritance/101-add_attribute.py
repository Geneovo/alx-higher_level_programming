#!/usr/bin/python3
"""Defines a function that adds attribute to objects"""


def add_attribute(obj, att, value):
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
