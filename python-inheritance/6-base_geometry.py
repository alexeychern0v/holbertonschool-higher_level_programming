#!/usr/bin/python3
"""Defines BaseGeometry"""


class BaseGeometry:
    """class for geometry objects"""

    def area(self):
        """Returns the area"""
        raise Exception("area() is not implemented")
