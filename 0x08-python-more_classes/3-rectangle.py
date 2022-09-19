#!/usr/bin/python3

"""This module contains `Rectangle` class."""


class Rectangle:
    """Use this class to create rectangles.

    Example:
        >>> rect = Rectangle()
    """
    def __init__(self, width=0, height=0):
        """Creates a new `Rectangle`.

        Args:
            width(int): The Rectangle width
            height(int): The Rectangle height

        Examples:
            >>> rect = Rectangle(1, 3)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the `width` of the `Rectangle`"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the `width` of the `Rectangle`"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the `height` of the `Rectangle`"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the `height` of the `Rectangle`"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the `area` of a `Rectangle`"""
        return self.width * self.height

    def perimeter(self):
        """Returns the `perimeter` of a `Rectangle`"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a `Rectangle` as string"""
        rect_str = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(0, self.height):
            if i > 0:
                rect_str += "\n"
            for j in range(0, self.width):
                rect_str += "#"
        return rect_str
