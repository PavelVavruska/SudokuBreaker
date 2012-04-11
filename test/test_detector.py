__author__ = '@PavelVavruska'

import unittest
from ..src.detector import Detector


class TestDetector(unittest.TestCase):
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

    def test_detector_row(self):

        self.assertEqual(Detector.free_in_row(TestDetector.test_sudoku, 0),
            [3, 4, 6, 8])

        self.assertEqual(Detector.free_in_row(TestDetector.test_sudoku, 8),
            [1, 3, 6, 7])

    def test_detector_column(self):

        self.assertEqual(Detector.free_in_column(TestDetector.test_sudoku, 0),
            [3, 5, 8, 9])

        self.assertEqual(Detector.free_in_column(TestDetector.test_sudoku, 8),
            [4, 5, 6, 8])

    def test_detector_squere3x3(self):

        self.assertEqual(Detector.free_in_squere3x3(
            TestDetector.test_sudoku, 0, 0), [1, 6, 8])

        self.assertEqual(Detector.free_in_squere3x3(
            TestDetector.test_sudoku, 8, 8), [4, 6, 7])

if __name__ == '__main__':
    unittest.main()
