from tkinter import Tk, BOTH, Canvas

class Window ():
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
        while(self.__isRunning):
            self.redraw()
    
    def close(self):
        self.__isRunning = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1: Point, point_2: Point):
        self.p1 = point_1
        self.x1 = self.p1.x
        self.y1 = self.p1.y

        self.p2 = point_2
        self.x2 = self.p2.x
        self.y2 = self.p2.y
    
    def draw(self, canvas: Canvas, color):
        canvas.create_line(
            self.x1, self.y1, self.y2, self.y2, fill= color, width = 2 
        )