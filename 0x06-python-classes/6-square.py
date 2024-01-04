#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize square
        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrives size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets value into size, must be integer
        Args:
            value (int0: size of the square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """retrives position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets value into position, must be tuple of 3 integers
        Args:
            value (tuple): position of the square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """returns the area

        Returns:
            the square of the siae
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square in #"""

        if self.__size != 0:
            for i in range(self.__position[1]):
                print()

                for i in range(self.__size):
                    print(' ' * self.__position[0], end='')
                    print('#' * self.__size)
        else:
            print()
