#!/usr/bin/python3
""" Module returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ Function retuns the dictionary description of an obj """

    resp = {}
    if hasattr(obj, "__dict__"):
        resp = obj.__dict__.copy()
    return resp
