#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 101):
        if c % 3 == 0 and c % 5 != 0:
            print("Fizz ", end='')
        elif c % 5 == 0 and c % 3 != 0:
            print("Buzz ", end='')
        elif c % 5 == 0 and c % 3 == 0:
            print("FizzBuzz ", end='')
        else:
            print("{}".format(c), end='')
