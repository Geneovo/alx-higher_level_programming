#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raised ValueError('size must be >= 0')

            self.__size = size
