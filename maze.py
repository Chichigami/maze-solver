from cell import *
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window,
    ):
        self.off_put_x = x1
        self.off_put_y = y1
        self.rows = num_rows
        self.cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = win
        self._create_cell()

    def _create_cell(self):
        self._cells = [[ Cell() for _ in range (self.rows)] for _ in range (self.cols)]

    def _draw_cell(self, i, j):
        
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        