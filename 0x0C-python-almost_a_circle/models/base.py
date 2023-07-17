#!/usr/bin/python3
""" Base Class Module """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to a file"""
        filename = cls.__name__+".json"
        with open(filename, 'w') as f:
            if not list_objs:
                json.dump([], f)
                return
            json.dump([obj.to_dictionary() for obj in list_objs], f)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all the attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(1, 1)
        if cls.__name__ == "Square":
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """loading dict representing the parameters for
            instances and from that creating instances"""
        filename = cls.__name__+".json"
        try:
            with open(filename, 'r') as f:
                content = cls.from_json_string(f.read())
        except Exception:
            return []
        return list(map(lambda obj: cls.create(**obj), content))
