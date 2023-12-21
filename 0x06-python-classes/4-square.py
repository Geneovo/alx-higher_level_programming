#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size: the size of the square defined
        """
        self.__size = size

    @property
    def size(self):
        """retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be integer
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area
        Returns:
            the square of the size
        """
        return self.__size ** 2
