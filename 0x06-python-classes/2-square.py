#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
        size mst be an integer, otherwise raise a TypeError exception
        if size is less than 0, raise a ValueError exception
"""


class Square:
    """this class instantiates an attribute and handles exceptions"""
    def __init__(self, size=0):
        """prints out custom error messages"""
        assert isinstance(size, int), f"size must be an integer"
        assert size >= 0, f"size must be >= 0"
        self.__size = size
