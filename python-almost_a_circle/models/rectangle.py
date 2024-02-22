#!/usr/bin/python3
from models.base import Base
"""Defines a Rectangle class"""


class Rectangle(Base): 
    """Inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets and sets value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Gets and sets value for heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Gets and sets value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Gets and sets value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value