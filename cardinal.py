from graphics import *
from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.__x1 = point_1.x
        self.__y1 = point_1.y

        self.__x2 = point_2.x
        self.__y2 = point_2.y
    
    def draw(self, canvas: Canvas, color):
        canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y2, fill= color, width = 2)