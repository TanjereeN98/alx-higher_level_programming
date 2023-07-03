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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing method"""
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

    def area(self):
        """returns rectangle area, duh"""
        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """__str__ representation"""
        s = ''
        if self.width == 0 or self.height == 0:
            return ""
        row = str(self.print_symbol) * self.width
        return "\n".join(row for _ in range(self.height))

    def __repr__(self):
        """__repr__ representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
