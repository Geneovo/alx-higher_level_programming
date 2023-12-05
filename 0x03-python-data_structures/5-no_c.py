#!/usr/bin/python3

def no_c(my_string):
    my_string_list = list(my_string)
    idx_count = 0

    for x in my_string_list:
        if x == 'c' or x == 'C':
            my_string_list[idx_count] = ""
        idx_count += 1

    return "".join(my_string_list)
