#!/usr/bin/python3
""" Base Class Module """


class Base:
    """Base class with private class attr and constructor"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Instantiating the class instaces"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
