from cardinal import *
from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    # cell_1 = Cell(win)
    # cell_1.draw(10, 10, 20, 20, False, False, True, True)
    # cell_2 = Cell(win)
    # cell_2.draw(20, 10, 30, 20, True, True, False, False)
    # cell_1.draw_move(cell_2)

    m1 = Maze(10, 10, 10, 10, 10, 10, win)
    print(m1._cells[0][0].has_top_wall)
    print(m1._cells[9][9].has_top_wall)
    win.wait_for_close()

main()