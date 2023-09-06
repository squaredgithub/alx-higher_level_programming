#!/usr/bin/python3
""" Module defines the class Student
"""


class Student:
    """ Class create student instances """

    def __init__(self, first_name, last_name, age):
        """ Method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method returns directory description """
        ob = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return ob

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in ob:
                    if attrs[iatr] == satr:
                        d_list[satr] = ob[satr]
            return d_list

        return ob
