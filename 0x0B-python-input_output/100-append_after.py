#!/usr/bin/python3
"""Module that appends a line after each occurence of a string"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a line after each occut=rence of a string
    Args:
        filename (str): Name of the file to update
        search_string (str): String to search for in the file
        new_string (str): string to append after each occurrence of earch_string
    """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(lines)
