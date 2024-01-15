#!/usr/bin/python3
"""define a locked class"""


class LockedClass:
    """a class with no class or object attributes that prevents
    the dynamic creation of new instance attributes except 'first_name'"""
    __slots__ = ["first_name"]
