#!/usr/bin/python3

if __name__ = "__main__":
    import sys
    x = 0
    for z in range(len(sys.argv) - 1):
        x += nt(sys.argv[z + 1])
    print("{}".format(x))
