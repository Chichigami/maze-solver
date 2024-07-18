from cardinal import *
from graphics import *

class Cell:
    def __init__(self, window: Window):
        self._win = window


    def draw(self, x_top_left, y_top_left, x_bottom_right, y_bottom_right, top_wall = True, right_wall = True, bottom_wall = True, left_wall = True):
        self.has_top_wall = top_wall
        self.has_right_wall = right_wall
        self.has_bottom_wall = bottom_wall
        self.has_left_wall = left_wall

        self.__top_left_point = Point(x_top_left, y_top_left)
        self.__top_right_point = Point(x_bottom_right, y_top_left)
        self.__bottom_left_point = Point(x_top_left, y_bottom_right)
        self.__bottom_right_point = Point(x_bottom_right, y_bottom_right)

        if self.has_top_wall:
            self._win.draw_line(Line(self.__top_left_point, self.__top_right_point))
        if self.has_right_wall:
            self._win.draw_line(Line(self.__top_right_point, self.__bottom_right_point))
        if self.has_bottom_wall:
            self._win.draw_line(Line(self.__bottom_right_point, self.__bottom_left_point))
        if self.has_left_wall:
            self._win.draw_line(Line(self.__top_left_point, self.__bottom_left_point))

    def draw_move(self, to_cell, undo = False):
        path = Line(self.middle_of_cell, to_cell.middle_of_cell)
        if undo:
            self.__win.draw_line(path, "gray")
        else:
            self.__win.draw_line(path, "red")