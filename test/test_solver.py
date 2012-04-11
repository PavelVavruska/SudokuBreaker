__author__ = '@PavelVavruska'

import unittest
from ..src.solver import Solver


class TestSolver(unittest.TestCase):
    test_sudoku = [
        [2, 5, 9, 7, 0, 0, 0, 1, 0],
        [4, 0, 3, 0, 0, 5, 9, 7, 0],
        [7, 0, 0, 3, 0, 4, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 8, 1],
        [0, 0, 5, 0, 2, 0, 4, 0, 0],
        [1, 8, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 1, 0, 8, 0, 0, 2],
        [0, 2, 7, 5, 0, 0, 1, 0, 3],
        [0, 4, 0, 0, 0, 2, 8, 5, 9],
    ]

    test_sudoku_result = [
        [2, 5, 9, 7, 8, 6, 3, 1, 4],
        [4, 6, 3, 2, 1, 5, 9, 7, 8],
        [7, 1, 8, 3, 9, 4, 6, 2, 5],
        [6, 3, 4, 9, 5, 7, 2, 8, 1],
        [9, 7, 5, 8, 2, 1, 4, 3, 6],
        [1, 8, 2, 4, 6, 3, 5, 9, 7],
        [5, 9, 6, 1, 3, 8, 7, 4, 2],
        [8, 2, 7, 5, 4, 9, 1, 6, 3],
        [3, 4, 1, 6, 7, 2, 8, 5, 9],
    ]

    def test_solver(self):
        """
              Testing of Sudoku one position solver:
              available choices at current position
              """
        self.assertEqual(Solver.free_at_position(TestSolver.test_sudoku, 1, 1),
                        [1, 6])

        self.assertEqual(Solver.free_at_position(TestSolver.test_sudoku, 7, 7),
                        [4, 6])

    def test_solving_sudoku(self):

        test_result = Solver.solve_sudoku(TestSolver.test_sudoku)
        self.assertEqual(test_result, TestSolver.test_sudoku_result)

if __name__ == '__main__':
    unittest.main()
