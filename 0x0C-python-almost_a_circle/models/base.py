#!/usr/bin/python3

"""Definiation the base model classes"""
import json
import csv
import turtle


class Base:
    """first the Base model.

    In project 0x0C*, this represents as the "base" for all other classes.

    Attributes of a Private Class:
        __nb_object (int): how many instantiated Bases there are.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init the new Base.

        Arguments as following:
            id (int): The new Base's identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a list of dicts serialised as JSON.

        Arguments as following:
            list_dictionaries (list): dictionaries that are listed.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A list of items should be serialised in JSON and written to a file.

        Arguments as following:
            list_objs (list): A list of of Base instances
		that have been inherited.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return JSON string's deserialization.

        Arguments as following:
            json_string (str): a list of dicts in a JSON str format.
        Return the below:
            An empty list if json_string is None or empty.
            If not, json_string will represent the Python list.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return the class that was created using a dictionary of attributes.

        Arguments as following:
            **dictionary (dict): Attribute key/value
		pairs that need to be initialised.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return the list of classes that were created
		from a JSON string database.

        Reads from `<cls.__name__>.json`.

        Returns as below:
            An empty list appears if the file is nonexistent.
            A list of instantiated classes, if not.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Create a file and serialise a list of items in CSV format.

        Args:
            list_objs (list): A list of Base instances that have been inherited.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return the list of classes that were created using a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns as below:
            An empty list appears if the file is nonexistent.
            A list of instantiated classes, if not.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """The turtle module can be used to draw squares and rectangles.

        Arguments as following:
            list_rectangles (list): a list of objects to draw in rectangles.
            list_squares (list): a list of objects to draw that are square.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
