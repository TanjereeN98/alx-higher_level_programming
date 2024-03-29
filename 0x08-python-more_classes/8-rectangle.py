#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                str_out += str(self.print_symbol)
            if i != self.__height - 1:
                str_out += "\n"
        return str_out

    def __repr__(self):
        """Object formal print format"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints when object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)
