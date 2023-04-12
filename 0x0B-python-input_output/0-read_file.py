#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """Reads from a file
    Args:
        filename: file
    Raises
        Exception: when file can be opened
    """

    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data, end='')
