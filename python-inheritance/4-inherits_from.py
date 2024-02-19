#!/usr/bin/python3
"""Defines inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class that 
    inherited (directly or indirectly) from the specified class"""

    return isinstance(obj, a_class) and type(obj) is not a_class
