#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    by using the inbuilt dir() method
    """
    return dir(obj)
