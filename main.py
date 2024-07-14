from tkclass import *


def main():
    win = Window(800, 600)
    p1 = Point(10, 49)
    p2 = Point(420, 69)
    pLine = Line(p1, p2)
    win.draw_line(pLine, "black")
    win.wait_for_close()

main()