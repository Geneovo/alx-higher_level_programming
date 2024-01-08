#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class inherited from a_class
    Otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
