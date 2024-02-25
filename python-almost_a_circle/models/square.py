#!/usr/bin/python3
from models.rectangle import Rectangle
"""Defines Square class"""


class Square(Rectangle):
    """Inherits from Base"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size> - in our case, width or height"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """Gets and sets width and height of rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
