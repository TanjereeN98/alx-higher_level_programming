#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            pass
        with open(cls.__name__+'.json', mode='w', encoding='utf-8') as fp:
            if list_objs is None:
                json.dump([], fp)
                return
