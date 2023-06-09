#!/usr/bin/python3
"""square class"""


class Square:
    """a Sqaue Class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square (default: 0).
            position (tuple): The position of the square (default: (0, 0)).
                              Should be a tuple of 2 positive integers.

        Raises:
            TypeError: If size is not an integer or  is not a tuple o
            ValueError: If size is less than 0.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.size * self.size

    def my_print(self):
        """
        Print the square using the character '#'.

        If the size is 0, it prints an empty line.
        The position is taken into account to determine the starting
        Lines before the square are filled with spaces based on the
        The number of empty lines before the square is determined

        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
