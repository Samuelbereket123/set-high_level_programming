#!/usr/bin/python3
"""Defines the Base model class."""


class Base:
    """Represent the base model for all other classes in this project.

    Attributes:
        __nb_objects (int): Number of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
