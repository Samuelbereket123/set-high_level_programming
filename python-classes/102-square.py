#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size: The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if this square's area equals another's."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if this square's area differs from another's."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if this square's area is greater than another's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square's area is >= another's."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if this square's area is less than another's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square's area is <= another's."""
        return self.area() <= other.area()
