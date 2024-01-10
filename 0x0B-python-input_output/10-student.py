#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization method for Student class
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Agr of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """Raises a dictionary representation of a student instance
            Args:
                attrs (list): List of attribute name to add
            Returns:
                dict: Dictionary representation of the student instance
            """
            if attrs in None:
                return self.__dict__
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
