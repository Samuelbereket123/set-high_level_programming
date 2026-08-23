#!/usr/bin/python3
"""
This module defines the Rectangle class.
The Rectangle class inherits from the Base class and represents a
four-sided geometric figure defined by width, height, and coordinates.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represent a Rectangle shape with attribute validation and operations.

    Inherits core ID handling from Base and defines width, height, x, and y
    with getter/setter validation rules.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X coordinate offset. Defaults to 0.
            y (int, optional): Y coordinate offset. Defaults to 0.
            id (int, optional): Unique identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle instance.

        Returns:
            int: The calculated area (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle instance using the '#' character.

        Takes into account the y offset (empty lines) and x offset (spaces).
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Assign positional or keyword arguments to attributes.

        Args:
            *args (list): Attribute values in order (id, width, height, x, y).
            **kwargs (dict): Key/value pairs of attributes to update.
        """
        attrs = ["id", "width", "height", "x", "y"]
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
        Return the dictionary representation of a Rectangle.

        Returns:
            dict: Dictionary containing id, width, height, x, and y.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the string representation of the Rectangle instance.

        Returns:
            str: Format '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
