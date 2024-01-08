#!/usr/bin/python3
"""Module for the Rectangle class, continuation of task 8"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""

    def __init__(self, width, height):
        """Initialization of a rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a rectangle string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height
