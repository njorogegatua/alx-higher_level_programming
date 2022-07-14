#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print(f"{length - 1} argument:")
        print(f"{length - 1}: {sys.argv[length - 1]}")
    else:
        ind = 0
        print(f"{length - 1} arguments:")
        for i in sys.argv:
            if ind == 0:
                ind = ind + 1
                continue
            print(f"{ind}: {sys.argv[ind]}")
            ind = ind + 1
