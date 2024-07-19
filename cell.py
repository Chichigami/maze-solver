from cardinal import *
from graphics import *

class Cell:
    def __init__(self, window: Window  = None):
        self._win = window

        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True


    def draw(self, x_top_left, y_top_left, x_bottom_right, y_bottom_right):
        self.__top_left_point = Point(x_top_left, y_top_left)
        self.__top_right_point = Point(x_bottom_right, y_top_left)
        self.__bottom_left_point = Point(x_top_left, y_bottom_right)
        self.__bottom_right_point = Point(x_bottom_right, y_bottom_right)

        if self.has_top_wall:
            self._win.draw_line(Line(self.__top_left_point, self.__top_right_point))
        else:
            self._win.draw_line(Line(self.__top_left_point, self.__top_right_point), "white")

        if self.has_right_wall:
            self._win.draw_line(Line(self.__top_right_point, self.__bottom_right_point))
        else:
            self._win.draw_line(Line(self.__top_right_point, self.__bottom_right_point), "white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(self.__bottom_right_point, self.__bottom_left_point))
        else:
            self._win.draw_line(Line(self.__bottom_right_point, self.__bottom_left_point), "white")

        if self.has_left_wall:
            self._win.draw_line(Line(self.__top_left_point, self.__bottom_left_point))
        else:
            self._win.draw_line(Line(self.__top_left_point, self.__bottom_left_point), "white")
        
        
        
        self.middle_of_cell = Point((x_top_left + x_bottom_right) / 2,  #this is for draw_move()
                                    (y_top_left + y_bottom_right) / 2)

    def draw_move(self, to_cell, undo = False):
        path = Line(self.middle_of_cell, to_cell.middle_of_cell)
        color = "red"
        if undo:
            color = "gray"
        self._win.draw_line(path, color)