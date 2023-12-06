#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    for element in set(my_list):
        x += element
    return x
