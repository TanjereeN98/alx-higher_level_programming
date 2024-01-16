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
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__+'.json', mode='w', encoding='utf-8') as fp:
            if list_objs is None:
                json.dump([], fp)
                return
            json.dump([json.loads(cls.to_json_string(obj.to_dictionary()))\
                        for obj in list_objs], fp)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            instance = Square(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode='r', encoding='utf-8') as fp:
                content = cls.from_json_string(fp.read())
        except NameError:
            return []
        return list(map(lambda x: cls.create(**x), content))
