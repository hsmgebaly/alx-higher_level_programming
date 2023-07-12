#!/usr/bin/python3
"""Defines Student's class."""


class Student:
    """Display a student."""

    def __init__(self, first_name, last_name, age):
        """Start a new Student.

        Arguments:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain the Student's definition in a dictionary.

        represents only those characteristics that are present in
        the list if attrs is a list of strings.


        Arguments:
            attrs (list): (Optional) The attr should be represented.

        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all of the Student's attrs.

        Arguments:
            json (dict): The key/value combinations to
            use in place of attributes.

        """
        for k, v in json.items():
            setattr(self, k, v)
