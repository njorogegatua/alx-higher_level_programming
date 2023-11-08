#!/usr/bin/python3
def best_score(a_dictionary):
    ref = 0
    while(a_dictionary):
        for key in a_dictionary.keys():
            value = a_dictionary[key]
            if value > ref:
                ref = value
                big = key
        return big
    else:
        return None
