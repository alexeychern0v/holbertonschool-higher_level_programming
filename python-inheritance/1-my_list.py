#!/usr/bin/python3
"""
Defines the class Mylist
"""


class MyList(list):
    """
    Implements sorted printing for the built-in list class
    """

    def print_sorted(self):
        """
        Print sorted list (ascenting order)
        """
        print(sorted(self))
