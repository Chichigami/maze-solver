from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze"
        self.__canvas = Canvas(self.__root, bg = "white", width = width, height = height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True
        while (self.__isRunning):
            self.redraw()
    
    def close(self):
        self.__isRunning = False

    def draw_line(self, line, color = "black"):
        line.draw(self.__canvas, color)

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
        if undo:
            Line(self.middle_of_cell, to_cell.middle_of_cell).draw(self.__win.__canvas, "gray")
        else:
            Line(self.middle_of_cell, to_cell.middle_of_cell).draw(self.__win.__canvas, "red")
    
