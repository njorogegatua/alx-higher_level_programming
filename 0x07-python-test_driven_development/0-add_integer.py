#!/usr/bin/python3

"""this module defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """addition function"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    num_1 = int(a)
    num_2 = int(b)
    return num_1 + num_2
