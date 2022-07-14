#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    count = 0
    for i in sys.argv:
        if count == 0:
            count += 1
            continue
        res += int(sys.argv[count])
        count += 1
    print("{}".format(res))
