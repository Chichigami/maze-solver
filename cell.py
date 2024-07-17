from cardinal import *
from graphics import *

class Cell:
    def __init__(self, x1, y1, x2, y2, window: Window, left_wall = True, right_wall = True, top_wall = True, bottom_wall = True):
        self.__has_left_wall = left_wall
        self.__has_right_wall = right_wall
        self.__has_top_wall = top_wall
        self.__has_bottom_wall = bottom_wall
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window

        self.__top_left_point = Point(self.__x1, self.__y1)
        self.__top_right_point = Point(self.__x2, self.__y1)
        self.__bottom_left_point = Point(self.__x1, self.__y2)
        self.__bottom_right_point = Point(self.__x2, self.__y2)

        self.middle_of_cell = Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2)
    
    def draw(self):
        if self.__has_left_wall:
            self.left_wall = Line(self.__top_left_point, self.__bottom_left_point)
            self.__win.draw_line(self.left_wall)
        if self.__has_right_wall:
            self.right_wall = Line(self.__top_right_point, self.__bottom_right_point)
            self.__win.draw_line(self.right_wall)
        if self.__has_top_wall:
           self.top_wall = Line(self.__top_left_point, self.__top_right_point)
           self.__win.draw_line(self.top_wall)
        if self.__has_bottom_wall:
            self.bottom_wall = Line(self.__bottom_left_point, self.__bottom_right_point)
            self.__win.draw_line(self.bottom_wall)

    def draw_move(self, to_cell, undo = False):
        path = Line(self.middle_of_cell, to_cell.middle_of_cell)
        if undo:
            self.__win.draw_line(path, "gray")
        else:
            self.__win.draw_line(path, "red")