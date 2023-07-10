#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args:
            (str) name: just a name
            (int) value: the validated variable

        Raise:
            ValueError: if value is less or equal to 0
            TypeError: if value is not an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
