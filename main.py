from cardinal import *
from graphics import *
from cell import *

def main():
    win = Window(800, 600)
    cell_1 = Cell(0, 0, 20, 20, win, top_wall= False, bottom_wall= False)
    cell_1.draw()
    cell_2 = Cell(0, 20, 20, 40, win, top_wall= False, right_wall= False)
    cell_2.draw()
    cell_1.draw_move(cell_2, True)
    win.wait_for_close()

main()