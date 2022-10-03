#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    r_width, r_height = 20, 4
    s_size = 10 


    # list_rectangles = [Rectangle(100, 40), Rectangle(100, 40, 0, 50), Rectangle(100, 40, 0, 100)]
    # list_squares = [Square(40, 0, 150), Square(40, 50, 150), Square(40, 100, 150)]

    # Border
    border = []
    # Left Border
    left_border = [Rectangle(r_height, r_width, 0, i * r_width) for i in range(1, 10)]
    # Right Border
    right_border = [Rectangle(r_height, r_width, 300, i * r_width) for i in range(1, 10)]
    # Top Border
    top_border = [Rectangle(r_width, r_height, i * r_width, 9 * r_width) for i in range(15)]
    # Bottom Border
    bottom_border = [Rectangle(r_width, r_height, i * r_width, 0) for i in range(15)]

    # Letters
    letters = []
    # Letter A
    letter_a = []
    a_left = [Square(s_size, i * 2, i * s_size) for i in range(4, 16)]
    a_right = [Square(s_size, 70 - (i * 2), i * s_size) for i in range(4, 16)]
    a_cross = [Square(s_size, s_size * i, 70) for i in range(2, 6)]

    # Letter L
    letter_l = []
    l_left = [Square(s_size, 80, i * s_size) for i in range(4, 16)]
    l_bottom = [Square(s_size, i + (s_size * (i - 80)), 4 * s_size) for i in range(80, 86)]


    # Letter X
    letter_x = []
    x_left = [Square(s_size, (i * 4) + (s_size * 5 + 86), i * s_size) for i in range(4, 16)]
    x_right = [Square(s_size, (80 - (i * 4)) + (s_size * 5 + 86), i * s_size) for i in range(4, 16)]

    Rectangle.save_to_file(bottom_border)
    border[:] = border + bottom_border
    border[:] = border + top_border
    border[:] = border + left_border
    border[:] = border + right_border


    letter_a[:] = letter_a + a_left
    letter_a[:] = letter_a + a_right
    letter_a[:] = letter_a + a_cross

    letter_l[:] = letter_l + l_left
    letter_l[:] = letter_l + l_bottom

    letter_x[:] = letter_x + x_left
    letter_x[:] = letter_x + x_right

    letters[:] = letters + letter_a + letter_l + letter_x
    Base.draw(border, letters)
