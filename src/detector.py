__author__ = '@PavelVavruska'


class Detector:
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @staticmethod
    def free_in_row(new_sudoku, y):
    # Searching for values in row
        now_available = Detector.available[:]
        for xx in range(0, 9):
            if new_sudoku[y][xx] in now_available:
                now_available.remove(new_sudoku[y][xx])
        return now_available

    @staticmethod
    def free_in_column(new_sudoku, x):
    # Searching for values in column
        now_available = Detector.available[:]
        for yy in range(0, 9):
            if new_sudoku[yy][x] in now_available:
                now_available.remove(new_sudoku[yy][x])
        return now_available

    @staticmethod
    def free_in_squere3x3(new_sudoku, y, x):
        # Searching for values in squere 3x3
        now_available = Detector.available[:]
        for yy in range(3 * (y / 3), 3 * (y / 3) + 3):
            for xx in range(3 * (x / 3), 3 * (x / 3) + 3):
                if new_sudoku[yy][xx] in now_available:
                    now_available.remove(new_sudoku[yy][xx])
        return now_available
