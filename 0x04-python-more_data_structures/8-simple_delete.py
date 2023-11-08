#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for x in list(a_dictionary):
        value = a_dictionary[x]
        if x == key:
            del a_dictionary[x]
    return a_dictionary
