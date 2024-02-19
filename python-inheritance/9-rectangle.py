#!/usr/bin/python3
""""Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns Rectangle width/height"""
        return f"[Rectangle] {self.__width}/{self.__height}"