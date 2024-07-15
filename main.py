from tkclass import *


def main():
    win = Window(800, 600)
    cell_1 = Cell(40, 40, 60, 60, win, False, True, False, True)
    cell_1.draw()
    win.wait_for_close()

main()