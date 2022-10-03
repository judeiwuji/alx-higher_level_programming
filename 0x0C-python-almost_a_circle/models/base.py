#!/usr/bin/python3

"""This module contains the `Base` model."""


import json
import csv
import turtle
import random


class Base:
    """This is the `Base` of all models."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Creates a `Model`.

        Args:
            id(int): The model id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries(list): list of dictionaries
        """

        if list_dictionaries is None or type(list_dictionaries) is not list:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): list of instances who inherits of Base
        """

        data = "[]"
        filename = cls.__name__ + ".json"
        if list_objs is not None and type(list_objs) is list:
            list_dict = []
            for obj in list_objs:
                if isinstance(obj, Base):
                    list_dict.append(obj.to_dictionary())
            data = cls.to_json_string(list_dict)
        with open(filename, encoding="utf-8", mode="w") as fp:
            fp.write(data)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation json_string.

        Args:
            json_string(str): a string representing a list of dictionaries
        """

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            dictionary(**): Keyword args
        """
        if len(dictionary) == 0:
            return
        dummy = cls(1, 1)
        update_data = {}
        attributes = ['id', 'width', 'height', 'size', 'x', 'y']
        for key in dictionary:
            if key in attributes:
                update_data[key] = dictionary[key]
        dummy.update(**update_data)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        objs = []
        try:
            filename = cls.__name__ + ".json"
            with open(filename, encoding="utf-8") as fp:
                data = cls.from_json_string(fp.read())
                for item in data:
                    objs.append(cls.create(**item))
        except FileNotFoundError:
            pass
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV

        Args:
            list_objs: A list of objects
        """

        filename = cls.__name__ + ".csv"
        with open(filename, encoding="utf-8", mode="w") as fp:
            writer = csv.writer(fp)
            rows = []
            if list_objs is not None and type(list_objs) is list:
                for obj in list_objs:
                    row = []
                    row.append(obj.id)
                    if cls.__name__ == "Rectangle":
                        row.append(obj.width)
                        row.append(obj.height)
                    if cls.__name__ == "Square":
                        row.append(obj.size)
                    row.append(obj.x)
                    row.append(obj.y)
                    rows.append(row)
                writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV."""

        objs = []
        fields = []
        if cls.__name__ == "Square":
            fields = ['id', 'size', 'x', 'y']
        if cls.__name__ == "Rectangle":
            fields = ['id', 'width', 'height', 'x', 'y']
        try:
            filename = cls.__name__ + ".csv"
            with open(filename, encoding="utf-8") as fp:
                reader = csv.reader(fp)
                for row in reader:
                    obj_dict = {}
                    for i, field in enumerate(fields):
                        obj_dict[field] = int(row[i])
                    objs.append(cls.create(**obj_dict))
        except FileNotFoundError:
            pass
        return objs

    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares.

        Args:
            list_squares(list): List of objects
        """
        fill_colors = ['red', 'blue', 'violet', 'tomato', 'skyblue']
        wn = turtle.Screen()
        wn.canvwidth = 400
        wn.canvheight = 400
        wn.window_height = 400
        wn.window_width = 400
        wn.title("Almost a Circle")
        turtle.Turtle()
        turtle.home()
        turtle.penup()

        for rect in list_rectangles:
            index = random.randint(0, len(fill_colors) - 1)
            turtle.penup()
            turtle.home()
            turtle.setx(rect.x)
            turtle.sety(rect.y)
            turtle.pendown()
            turtle.fillcolor(fill_colors[index])
            turtle.begin_fill()

            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)

            turtle.right(90)
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)

            turtle.end_fill()

        for square in list_squares:
            index = random.randint(0, len(fill_colors) - 1)
            turtle.penup()
            turtle.home()
            turtle.setx(square.x)
            turtle.sety(square.y)
            turtle.pendown()
            turtle.fillcolor(fill_colors[index])
            turtle.begin_fill()

            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)

            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)

            turtle.end_fill()
        turtle.hideturtle()
        turtle.done()
