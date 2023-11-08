#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    a_set = set()
    for elem in my_list:
        a_set.add(elem)
    for i in a_set:
        res += i
    return res
