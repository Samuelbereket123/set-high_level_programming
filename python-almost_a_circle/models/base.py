#!/usr/bin/python3
"""
This module defines the Base class.
The Base class serves as the base for all other classes in this project.
It manages id attribute assignment across all instances to avoid duplication.
"""
import json


class Base:
    """
    Base class for managing id attribute assignment across subclasses.

    Attributes:
        __nb_objects (int): Private class attribute tracking created objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): Unique identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries,
                 or '[]' if list_dictionaries is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = "{}.json".format(cls.__name__)
        dict_list = []
        if list_objs is not None:
            dict_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(dict_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)
