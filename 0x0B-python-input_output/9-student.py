#!/usr/bin/python3
"""Defines Student's class."""


class Student:
    """Display a student."""

    def __init__(self, first_name, last_name, age):
        """start a new Student.

        Arguments:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Find a definition of the student in a dictionary."""
        return self.__dict__
