#!/usr/bin/python3
""" Module a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Function returns an object by a JSON representation
    Args:
        my_str: JSON rep
    Raises:
        Exception: when string can't be decoded
    """
    return json.loads(my_str)
