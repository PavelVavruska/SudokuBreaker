__author__ = 'develop'

from src.solver import Solver
from src.views import write_it_down
from src.utils.colors import bcolors

error_msg = '\nCode execution has been interrupted: ' \
            'Input sudoku is not in correct shape 9x9 numbers.'

def main():
    error_detected = False
    """
    Reading sudoku file
    """
    try:
        with open("static/sudoku.txt") as file:
            file_sudoku = [line.split() for line in file]
    except:
        bcolors.printError('\nFile sudoku.txt does not exist or is corrupted.')
        error_detected = True
    """
    Validation and conversion of sudoku file into 2D integer array
    """
    if not error_detected:
        if len(file_sudoku) == 9:
            for yy in range(9):
                row_lenght = 0
                for xx in range(9):
                    row_lenght += 1
                    file_sudoku[yy][xx] = int(file_sudoku[yy][xx])
                if row_lenght != 9:
                    error_detected = True
        else:
            error_detected = True
    """
    Execution of program logic: Solving sudoku
    """
    if not error_detected:
        bcolors.printOK_BOLD('\nInput sudoku:\n')
        write_it_down(file_sudoku)
        bcolors.printOK_BOLD('\nSolved sudoku:\n')
        write_it_down(Solver.solve_sudoku(file_sudoku))
    else:
        bcolors.printError(error_msg)

if __name__ == '__main__':
    main()