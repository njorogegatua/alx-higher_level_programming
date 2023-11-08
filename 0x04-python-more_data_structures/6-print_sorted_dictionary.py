#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {}
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        sorted_dict[key] = value
    for x, y in sorted_dict.items():
        print(f"{x}: {y}")
