#!/usr/bin/python3
"""This defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """A class that reprents a base geometry"""

    def area(self):
        """"Raises an exception with a specific message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value parameter as an integer"""
        if type(value) != int
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
