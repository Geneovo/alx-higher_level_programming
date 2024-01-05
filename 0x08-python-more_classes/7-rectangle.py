#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of this rectangle class
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string rep of the rectangle"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for x in range(self.__height):
            for z in range(self.__width):
                rect = rect + str(self.print_symbol)
            if x != self.__height - 1:
                rect = rect + '\n'
        return rect

    def __repr__(self):
        """Return string rep of rectangle"""
        x = "Rectangle(" + str(self.__width) + ', ' + str(self.__height) + ')'
        return x

    def __del__(self):
        """Prints a message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
