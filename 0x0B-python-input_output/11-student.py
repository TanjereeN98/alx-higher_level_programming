#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """The Student Class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) \
                and all(isinstance(item, str) for item in attrs):
            new_dict = {}
            for key in attrs:
                value = self.__dict__.get(key)
                if value:
                    new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
