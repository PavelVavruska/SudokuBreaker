__author__ = 'develop'

from src.utils.colors import bcolors

# Output method
def write_it_down(own_sudoku_array):
    print
    for x in range(0,9):
        for y in range(0,9):
            if (y) % 3 == 0 or (x + 1) % 3 == 0 and x != 0:
                if own_sudoku_array[x][y] != 0:
                    bcolors.printOK_BOLD('%3.3s' %(own_sudoku_array[x][y]))
                else:
                    bcolors.printWarning_BOLD('%3.3s' %(own_sudoku_array[x][y]))
            else:
                if own_sudoku_array[x][y] != 0:
                    bcolors.printOK('%3.3s' %(own_sudoku_array[x][y]))
                else:
                    bcolors.printWarning('%3.3s' %(own_sudoku_array[x][y]))
        print
    return True