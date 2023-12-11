#!/usr/bin/python3

"""write a class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """import from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """call the super method"""
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    # print readable format
    def __str__(self):
        return f'[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}'

    # getter method for size
    @property
    def size(self):
        return self.__width

    # setter method for size
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    # return dictionary representation
    def to_dictionary(self):
        
        """return dictionary representation of a square"""
        return {'id': self.id, 'x': self.__x,
                'size': self.__width, 'y': self.__y}

    def update(self, *args, **kwargs):
        
        """assign attributes using args and kwargs"""
        i = 0
        if len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.__x = arg
                elif i == 3:
                    self.__y = arg
                i += 1
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v
