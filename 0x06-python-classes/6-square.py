#!/usr/bin/python3

"""This module contains the definition of a Square"""


class Square:
    """A Square class will be used to create a square shape."""

    def __init__(self, size=0, position=(0, 0)):
        """Intantiates a square object.

        Args:
            size (int): the size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the area of a square."""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of this square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of this square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints this square"""
        if self.size > 0:
            for i in range(0, self.size):
                for m in range(0, self.position[0]):
                    if self.position[1] <= 0:
                        print(end=" ")
                for j in range(0, self.size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """Returns this square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets this square position"""
        if (type(value) is tuple) and (len(value) == 2):
            x, y = value
            if (type(x) is int) and (type(y) is int):
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 \
                                positive integers")
        else:
            raise TypeError("position must be a tuple of 2 \
                                positive integers")
