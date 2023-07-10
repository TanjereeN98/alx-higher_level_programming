#!/usr/bin/python3
"""Rectangle Derived Class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle SubClass from BaseGeometry"""
    def __init__(self, width, height):
        """Self instantiation"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
