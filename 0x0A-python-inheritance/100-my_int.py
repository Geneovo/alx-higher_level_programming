#!/usr/bin/python3
"""Module that defines a class MyInt that inherits from int"""


class MyInt(int):
    """A class that inherits from int with inverted operators == and !="""
    def __eq__(self, value):
        """Invert == operator"""
        return self.real != value

    def __ne__(self, value):
        """ this will invert != operator"""
        return self.real == value
