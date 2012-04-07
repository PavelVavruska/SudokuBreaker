__author__ = 'develop'

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

    def test_solver(self):

        self.assertEqual(Solver.free_at_position(TestSolver.test_sudoku, 1, 1), [1, 6])

        self.assertEqual(Solver.free_at_position(TestSolver.test_sudoku, 7, 7), [4, 6])

    def test_solving_sudoku(self):

        test_result = Solver.solve_sudoku(TestSolver.test_sudoku)
        self.assertEqual(test_result, TestSolver.test_sudoku)


if __name__ == '__main__':
    unittest.main()
