#!/usr/bin/python3
"""Module that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a text file
    Args:
        filename (str): Name of the file to append
        text (str): Text to append to the file
    Returns:
        int: Number of characters written
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
