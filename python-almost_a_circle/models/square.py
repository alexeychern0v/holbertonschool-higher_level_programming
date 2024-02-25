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
    
    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                if i == "size":
                    self.size = kwargs[i]
                if i == "x":
                    self.x = kwargs[i]
                if i == "y":
                    self.y = kwargs[i]
    