#!/usr/bin/python3
"""Module that contains a function thaat reads file and prints to stdout"""


def read_file(filename=""):
    """Reads and prints text file cwith utf-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
