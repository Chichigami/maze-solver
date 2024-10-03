from cardinal import *
from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    m1 = Maze(10, 10, 12, 10, 10, 10, win, 0)

    win.wait_for_close()

main()