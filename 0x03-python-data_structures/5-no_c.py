#!/usr/bin/python3
def no_c(my_string):
    new_string = [d for d in my_string if d != 'C' and d != 'c']
    return ("".join(new_string))
