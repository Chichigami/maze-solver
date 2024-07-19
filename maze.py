from cell import *
from graphics import *
from cardinal import *
import time

class Maze:
    def __init__(self, start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, window: Window = None):
        self.off_put_x = start_x
        self.off_put_y = start_y

        self.rows = num_rows
        self.cols = num_cols

        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = window

        self._cells = []
        self._create_cell()
        self._break_entrance_and_exit()

    def _create_cell(self):
        #2D list. col is top level
        self._cells = [[ Cell(self.win) for _ in range (self.rows)] for _ in range (self.cols)]

        for col in range(self.cols):
            for row in range(self.rows):
                self._draw_cell(col, row)
    
    def _break_entrance_and_exit(self):
        #entrance top left cell and exit bottom right cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.cols-1][self.rows-1].has_bottom_wall = False
        self._draw_cell(self.cols-1, self.rows-1)

    def _draw_cell(self, i, j):
        if self.win is None:
            return 
        
        #top left x, y
        x1 = self.off_put_x + i * self.size_x
        y1 = self.off_put_y + j * self.size_y
        #bottom right x, y
        x2 = x1 + self.size_x
        y2 = y1 + self.size_y

        #self._cells[i][j] is a Cell(win)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        #time.sleep(0.05)
    
