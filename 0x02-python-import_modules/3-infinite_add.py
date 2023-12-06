#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    for z in range(len(sys.argv) - 1):
        x += int(sys.argv[z + 1])
    print("{}".format(x))
