#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    count = len(sys.argv) - 1
    while count == 3:
        if sys.argv[2] == '+':
            arg1 = int(sys.argv[1])
            arg2 = int(sys.argv[3])
            result = add(arg1, arg2)
            print(f"{sys.argv[1]} + {sys.argv[3]} = {result}")
            break
        elif sys.argv[2] == '-':
            arg1 = int(sys.argv[1])
            arg2 = int(sys.argv[3])
            result = sub(arg1, arg2)
            print(f"{sys.argv[1]} - {sys.argv[3]} = {result}")
            break
        elif sys.argv[2] == "*":
            arg1 = int(sys.argv[1])
            arg2 = int(sys.argv[3])
            result = mul(arg1, arg2)
            print(f"{sys.argv[1]} * {sys.argv[3]} = {result}")
            break
        elif sys.argv[2] == '/':
            arg1 = int(sys.argv[1])
            arg2 = int(sys.argv[3])
            result = div(arg1, arg2)
            print(f"{sys.argv[1]} / {sys.argv[3]} = {result}")
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
