#!/usr/bin/python3
"""Rectangle Module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String Representation of the object"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def area(self):
        """Return the area of Rectangle"""
        return self.__width * self.__height
