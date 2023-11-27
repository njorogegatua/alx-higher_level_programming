#!/usr/bin/python3

"""a class Rectangle with two private attributes"""


class Rectangle:
    """a class that has two private instance attributes, setters and getters"""
    # a public class attribute
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width and self.__height == 0:
            return (0)
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width and self.__height == 0:
            return("")
        else:
            rect = []
            for row in range(0, self.__height):
                for col in range(0, self.__width):
                    rect.append(Rectangle.print_symbol)
                if row != self.__height - 1:
                    rect.append('\n')
            return("".join(rect))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        rec1 = rect_1.area()
        rec2 = rect_2.area()
        if rec1 >= rec2:
            return rec1
        return rec2

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(width, height)
