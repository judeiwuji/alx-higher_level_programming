#!/usr/bin/python3

"""This module contains ``Square`` class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Creates a Square.

        Args:
            size(int): the size of the `square`
            x(int): The x axis of the `square`
            y(int): The y axis of the `square`
            id(int|Any): The id of the `square`
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                       self.y, self.width)

    @property
    def size(self):
        """Returns the size of the `square`."""

        return super().width

    @size.setter
    def size(self, value):
        """Sets the square size.

        Args:
            size(int): The size of the square
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes.

        Args:
            args(*): A variadic arguments represented as tuple
            kwargs(**): A variadic arguments represented as dictionary
        """

        if args is not None:
            attributes = ['id', 'size', 'x', 'y']

            for i, arg in enumerate(args):
                if i > len(attributes):
                    break
                setattr(self, attributes[i], arg)

        if (args is None or len(args) == 0) and kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns the dictionary representation of a Square."""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
