#!/usr/bin/python3
"""Private instance attribute: size:

    property def size(self): to retrieve it
    prop setter def size(self, value): to set it:
        size must be an integer, otherwise raise a TypeError
        if size is less than 0, raise a ValueError

Private instance attribute: position:

    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
        position must be a tuple of 2 positive integers
"""


class Square:
    """the Square class uses getter and setter methods"""
    def __init__(self, size=0, position=(0, 0)):
        assert isinstance(size, int), f'size must be an integer'
        assert size >= 0, f'size must be >= 0'

        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), f'size must be an integer'
        assert value >= 0, f'size must be >= 0'

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TyperError("position must be a tuple of two integers")

        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        else:
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(' ', end="")
                for j in range(0, self.__size):
                    print('#', end="")
                print()
