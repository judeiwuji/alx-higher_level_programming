#!/usr/bin/python3

"""This module contains the `Base` model."""


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
