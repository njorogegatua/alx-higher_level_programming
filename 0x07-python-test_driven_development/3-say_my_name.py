#!/usr/bin/python3

"""function tha prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """make sure the arguments are strings"""
    if type(first_name) not in [str]:
        raise TypeError('first_name must be a string')
    if type(last_name) not in [str]:
        raise TypeError('last_name must be a string')
    if len(first_name) > 20:
        raise OverflowError('first_name is too long')
    if len(last_name) > 20:
        raise OverflowError('last_name is too long')
    print(f"My name is {first_name} {last_name}")
