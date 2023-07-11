#!/usr/bin/python3
"""Student Class"""


class Student:
    """representation of the student"""
    def __init__(self, first_name, last_name, age):
        """init the obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to json"""
        _dict = self.__dict__
        if attrs is None:
            return _dict
        new_dict = {}
        for key in attrs:
            new_dict[key] = _dict.get(key)
        return new_dict
