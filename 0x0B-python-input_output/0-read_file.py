#!/usr/bin/python3
"""Module that contains a function thaat reads file and prints to stdout"""


def read_file(filename=""):
    """Reads and prints text file content in stdout
    Args:
        filename (str): Name of the file to read
    """
    with open(filename, encoding='utf-8') as file
    print(file.read(), end="")
