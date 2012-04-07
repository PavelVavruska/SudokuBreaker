__author__ = 'develop'

from detector import Detector

class Solver:
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @staticmethod
    def free_at_position(new_sudoku, y, x):
        now_available = Solver.available[:]

        init_avail = set(now_available)
        first_step_avail = init_avail.intersection(Detector.free_in_column(new_sudoku, x))
        second_step_avail = first_step_avail.intersection(Detector.free_in_row(new_sudoku, y))
        third_step_avail = second_step_avail.intersection(Detector.free_in_squere3x3(new_sudoku, y, x))
        return list(third_step_avail)

    @staticmethod
    def solve_sudoku(new_sudoku):
        """
              This methods solves sodoku by scanning the whole 2D array
              and replacing zeros with correct numbers.
              """
        for yy in range(9): # first vertical
            for xx in range(9): # second horizontal
                if new_sudoku[yy][xx] == 0:
                    now_available = Solver.free_at_position(new_sudoku, yy, xx)
                    if len(now_available) == 1:
                        new_sudoku[yy][xx] = now_available[0]
                        Solver.solve_sudoku(new_sudoku)



        return new_sudoku



