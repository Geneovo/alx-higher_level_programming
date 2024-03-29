#!/usr/bin/python3
"""Module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a new square

        Args:
            size (int): The size of the new square
            x (int): The x coordinate of the new square
            y (int): The y coordinate of the new square
            id (int): The identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes to the instance

        Args:
            *args (ints): New attribute values
            - 1st arguent represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute

            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.size, self.x, sellf.y)
                        else:
                            self.id = v
                    elif k == "size":
                        self.size = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def __str__(self):
        """Return a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
