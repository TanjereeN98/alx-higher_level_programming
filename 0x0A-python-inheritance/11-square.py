#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """sub class Square"""
    def __init__(self, size):
        """Initialize the square"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """Square Area"""
        return self.__size * self.__size

    def __str__(self):
        """print format of the square"""
        return f"[Square] {self.__size}/{self.__size}"
