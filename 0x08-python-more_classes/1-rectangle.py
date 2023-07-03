#!/usr/bin/python3
"""A Rectangele module"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle

    Args:
    int (width): width of the rectangle
    int (height): height of the rectangle, duh!

    raises:
    TypeError if width/height isn't an integer
    ValueError if width/height is less than 0
    """
    def __init__(self, width=0, height=0):
        """initializing method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height getter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
