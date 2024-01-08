#!/usr/bin/python3
"""Module that defines a Square class that inherits from the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialization of a square instance
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the square look"""
        return "[Square] {}/{}".format(self.__width, self.__height)
