#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiation"""
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
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """object print format"""
        if self.__width == 0 or self.__height == 0:
            return ""
        str_out = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_out += "#"
            if i != self.__height - 1:
                str_out += "\n"
        return str_out

    def __repr__(self):
        """Object formal print format"""
        return f"Rectangle({self.__width}, {self.__height})"
