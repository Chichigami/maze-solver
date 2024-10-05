from typing import List, Tuple
from cell import *
import time
import random

class Maze:
  def __init__(self, start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, window: Window = None, seed = None):
    self.off_put_x = start_x
    self.off_put_y = start_y
    self.rows = num_rows
    self.cols = num_cols
    self.size_x = cell_size_x
    self.size_y = cell_size_y
    self.win = window
    self._cells = []
    if seed:
        random.seed(seed)
  

    self._create_cell()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()

  def _create_cell(self):
      #2D list. col is top level
      self._cells: List[List[Cell]] = [[ Cell(self.win) for _ in range (self.rows)] for _ in range (self.cols)]

      for col in range(self.cols):
          for row in range(self.rows):
              self._draw_cell(col, row)
    

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
  
  def _break_entrance_and_exit(self):
      #entrance top left cell and exit bottom right cell
      self._cells[0][0].has_top_wall = False
      self._draw_cell(0,0)
      self._cells[self.cols-1][self.rows-1].has_bottom_wall = False
      self._draw_cell(self.cols-1, self.rows-1)
    
  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
      need_to_visit = []
    
      for a, b, wall in [(-1, 0, 'left'), (0, -1, 'top'), (1, 0, 'right'), (0, 1, 'bottom')]:
        ni, nj = i + a, j + b
        if (0 <= ni < self.cols and 0 <= nj < self.rows) and not self._cells[ni][nj].visited:
          need_to_visit.append((ni, nj, wall))

          
      if not need_to_visit:
        self._draw_cell(i, j)
        return

      ni, nj, wall = random.choice(need_to_visit)
      match wall:
        case 'top':
          self._cells[i][j].has_top_wall = False
          self._cells[ni][nj].has_bottom_wall = False
        case 'left':
          self._cells[i][j].has_left_wall = False
          self._cells[ni][nj].has_right_wall = False
        case 'bottom':
          self._cells[i][j].has_bottom_wall = False
          self._cells[ni][nj].has_top_wall = False
        case 'right':
          self._cells[i][j].has_right_wall = False
          self._cells[ni][nj].has_left_wall = False
        case _:
          raise Exception("breaking wall error")

      self._break_walls_r(ni, nj)

  def _reset_cells_visited(self):
    for cells in self._cells:
      for cell in cells:
        cell.visited = False

  def solve(self):
    return self._solve_r(0, 0)

  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True
    if i == self.cols-1 and j == self.rows-1:
      return True
     
    for a, b, wall in [(-1, 0, self._cells[i][j].has_left_wall), (1, 0, self._cells[i][j].has_right_wall), 
                       (0, -1, self._cells[i][j].has_top_wall), (0, 1, self._cells[i][j].has_bottom_wall)]:
      ni, nj = i + a, j + b
      if (0 <= ni < self.cols and 0 <= nj < self.rows) and not self._cells[ni][nj].visited and wall is False:
        self._cells[i][j].draw_move(self._cells[ni][nj])
        if self._solve_r(ni, nj):
          return True
        else:
          self._cells[i][j].draw_move(self._cells[ni][nj], True)

    return False