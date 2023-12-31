#!/usr/bin/python3
"""
Module to add two integers a and b
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b

    Args:
        a (int or float): The first number
        b (int or float): The second number

    Returns:
        int: The addition of a and b

    Raises:
        TypeError: If a or b is not an int or a float
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
