#!/usr/bin/python3
"""Module that defines a Square class that inherits from the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class"""

    def __init__(self, size):
        """Initializes a Square instance
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
