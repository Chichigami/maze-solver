from cell import *
import time

class Maze:
    def __init__(self, start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, win: Window):
        self.off_put_x = start_x
        self.off_put_y = start_y

        self.rows = num_rows
        self.cols = num_cols

        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = win

        self._create_cell()

    def _create_cell(self):
        #2D list. col is top level
        self._cells = [[ Cell(self.win) for _ in range (self.rows)] for _ in range (self.cols)]

        for col in range(self.cols):
            for row in range(self.rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        x1 = self.off_put_x + i * self.size_x
        y1 = self.off_put_y + j * self.size_y
        x2 = x1 + self.size_x
        y2 = y1 + self.size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        