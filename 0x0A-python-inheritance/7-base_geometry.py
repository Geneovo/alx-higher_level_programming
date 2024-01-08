#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A class with area and integer_validator methods"""
    def area(self):
        """"Raises an exception with a specific message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value parameter"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
