#!/usr/bin/python3

if _name_ == "_main_":
    from add_0 import add
    a = 1
    b = 2
    res = add (a, b)
    print("{:d} + {:d} = {:d}".format(a, b, res))
