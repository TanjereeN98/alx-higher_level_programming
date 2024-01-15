#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of the Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Representation of the Square instance"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update method of the sqaure"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        my_dict = {
            'id': getattr(self, 'id'),
            'x': getattr(self, 'x'),
            'size': getattr(self, 'size'),
            'y': getattr(self, 'y')
        }
        return my_dict
