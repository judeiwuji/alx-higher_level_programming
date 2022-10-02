#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(100, 40, 0, 50), Rectangle(100, 40, 0, 100)]
    list_squares = [Square(40, 0, 150), Square(40, 50, 150), Square(40, 100, 150)]

    Base.draw(list_rectangles, list_squares)
