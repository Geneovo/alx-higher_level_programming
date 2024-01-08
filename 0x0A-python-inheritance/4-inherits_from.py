#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class inherited from a_class
    Otherwise False
    """
    return issubclass(type(obj), a_class)
