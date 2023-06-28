#!/usr/bin/python3
"""square class"""


class Square:
    """a Sqaue Class"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing instance"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(num, int) and num > 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#'"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
