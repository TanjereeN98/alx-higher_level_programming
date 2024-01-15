#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " " + "#" * self.__width)

    def __str__(self):
        """Representation of the Rectangle instance"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
                {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        my_dict = {
            'x': getattr(self, 'x'),
            'y': getattr(self, 'y'),
            'id': getattr(self, 'id'),
            'height': getattr(self, 'height'),
            'width': getattr(self, 'width')
        }
        return my_dict
