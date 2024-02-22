#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    """Defines private class atribute nb objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
