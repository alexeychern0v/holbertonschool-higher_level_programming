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
        
    @width.setter
    def width(self, value):
        """If value is not int or under or equals 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets and sets value for heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        
    @height.setter
    def height(self, value):
        """If value is not int or under or equals 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets and sets value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.setter
    def x(self, value):
        """If value is not int or under 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__width = value
        
    @property
    def y(self):
        """Gets and sets value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        
    @y.setter
    def y(self, value):
        """If value is not int or under 0"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__width = value
        
    def area(self):
        """Returns the area value of the rectangle"""
        
        return (self.__width * self.__height)
    
    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))
            
    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        
    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
                
    