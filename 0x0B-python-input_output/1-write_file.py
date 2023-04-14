#!/usr/bin/python3
""" Module has a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ Function to writes to a text file
    Args:
        filename: file
        text: text to write
    Raises
        Exception: when the file can open
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
