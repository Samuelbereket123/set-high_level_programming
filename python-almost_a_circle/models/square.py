#!/usr/bin/python3
"""
This module defines the Square class.
The Square class inherits directly from the Rectangle class
and provides specialized attributes and behavior for square shapes.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a Square shape that inherits from Rectangle.

    A Square is a special type of Rectangle where width and height are equal.
    It manages size, position (x, y), and identification attributes.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The width and height of the square.
            x (int, optional): The horizontal offset coordinate. Defaults to 0.
            y (int, optional): The vertical offset coordinate. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get or set the size of the square.

        When setting size, both width and height are assigned the same value.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square instance.

        Args:
            *args (list): Positional arguments in order: id, size, x, y.
            **kwargs (dict): Keyword arguments representing attribute names
                and their corresponding values.
        """
        attrs = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for idx, arg in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the string representation of the Square instance.

        Returns:
            str: Format '[Square] (<id>) <x>/<y> - <size>'
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
