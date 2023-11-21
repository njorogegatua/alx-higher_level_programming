#!/usr/bin/python3
"""Write a class Square that defs a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
"""


class Square:
    """a class that has a private instance attribute"""
    def __init__(self, size):
        """this method initializes size as a private inst"""
        self.__size = size
