#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization method for student class
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a student instance
        Args:
            attrs (list): List of attribute names to add
        Returns:
            dict: Dictionary representation of the student instance
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
