import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):   
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_entrance_and_exit(self):   
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False,
        )
    
    def test_visited(self):
        num_rows = 12
        num_cols = 16
        margin = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows

        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y)
        for cells in maze._cells:
            for cell in cells:
                self.assertEqual(cell.visited, False)

if __name__ == "__main__":
    unittest.main()
