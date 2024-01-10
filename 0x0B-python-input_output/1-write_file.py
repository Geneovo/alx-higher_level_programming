#!/usr/bin/python3
"""Module defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text files
    Returns the number of characters written
    Args:
        filename (str): Name of the file to write
        text (str): Text to write to the file
    Returns:
        int: Number of characters written
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
