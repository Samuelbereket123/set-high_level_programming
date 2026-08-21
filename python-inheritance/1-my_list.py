#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """A class that inherits from list with additional methods."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
