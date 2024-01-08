#!/usr/bin/python3
"""Square Module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New Square Class"""
    def __init__(self, size):
        """Instantiation with Size"""
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """String Representation of the object"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def area(self):
        """Square Area Method"""
        return self.__size ** 2
