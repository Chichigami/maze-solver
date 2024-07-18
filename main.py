from cardinal import *
from graphics import *
from cell import *

def main():
    win = Window(800, 600)

    cell_1 = Cell(win)
    cell_1.draw(10, 10, 20, 20, False, False, True, True)
    cell_2 = Cell(win)
    cell_2.draw(20, 10, 30, 20, True, True, False, False)

    win.wait_for_close()

main()