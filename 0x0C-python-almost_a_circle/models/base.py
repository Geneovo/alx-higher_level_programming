#!/usr/bin/python3
"""Module that defines the Base class"""
import json
import csv
import turtle


class Base:
    """Represents the base class model.

    This represents the "base" for all other classes in this project

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a new Base

        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries
        Returns:
            str: The JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file

        Args:
            list_objs (list): A list of inherited Base instance
        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the JSON string deserialization

        Args:
            json_string (str): A JSON str representation of a list of dicts
        Returns:
            if json_string is None or an empty list
            otherwise - thee python list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set

        Args:
            **dictionary: A dictionary representing the attributes
        Returns:
            Base: An instance with all attributes set
        """
        if dictionary and dictionary != {}:
            if cls.__name_- == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file

        Reads from `<cls.__name__>.json`

        Returns:
            if the file does not exist - an empty list
            otherwise - a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
