#!/usr/bin/python3
def no_c(my_string):
    updated_str = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            updated_str += x
        return (updated_str)
