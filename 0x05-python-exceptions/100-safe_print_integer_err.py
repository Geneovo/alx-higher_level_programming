#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        reture True
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return False
