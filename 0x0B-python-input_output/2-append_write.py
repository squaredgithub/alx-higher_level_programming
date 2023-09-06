#!/usr/bin/python3
""" Module has a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file
    Args:
        filename: file
        text: text to write
    Raises
        Exception: when file can op
    """

    with open(filename, 'p', encoding="utf-8") as file:
        return file.write(text)
