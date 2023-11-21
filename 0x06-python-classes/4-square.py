#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        prop setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError
            if size is less than 0, raise a ValueError
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): returns the square area
"""


class Square:
    """the Square class uses getter and setter methods"""
    def __init__(self, size=0):
        assert isinstance(size, int), f'size must be an integer'
        assert size >= 0, f'size must be >= 0'
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), f'size must be an integer'
        assert value >= 0, f'size must be >= 0'

        self.__size = value

    def area(self):
        return self.__size * self.__size
