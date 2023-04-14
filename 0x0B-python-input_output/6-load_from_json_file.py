#!/usr/bin/python3
""" Module creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function creates an Object from a JSON file
    Args:
        filename: textfile name
    Raises:
        Exception: when object can't be encoded
    """
    with open(filename, 'rt', encoding="utf-8") as file:
        return json.load(file)
