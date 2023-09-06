#!/usr/bin/python3
""" Module has a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """ Function returns the JSON representation of an object
    Args:
        my_obj: object
    Raises:
        Exception: when object can't be encoded
    """
    return json.dumps(my_obj)
