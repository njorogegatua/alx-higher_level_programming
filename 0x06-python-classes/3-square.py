#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
        size must be an integer, otherwise raise a TypeError
        if size s less than 0, raise a ValueError
    Public instance method: def area(self): returns the square area
"""


class Square:
    """a class that contains methods and instances"""
    def __init__(self, size=0):
        assert isinstance(size, int), f"size must be an integer"

        assert size >= 0, f"size must be >= 0"
        self.__size = size

    def area(self):
        return self.__size * self.__size
