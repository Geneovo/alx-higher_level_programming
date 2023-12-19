#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        total = fct(*args)
        return total
    except Exception as x:
        sys.stderr.write("Exception: {}\n".format(x))
        return None
