#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x in list(a_dictionary):
        if a_dictionary.get(x) == value:
            del a_dictionary[x]
    return a_dictionary
