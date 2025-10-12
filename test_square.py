import unittest
import math
from square import square_area, square_perimeter


class TestSquare(unittest.TestCase):

    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_square_area_positive(self):
        self.assertEqual(square_area(5), 25)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            square_area(-1)

    def test_square_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square_perimeter(-10)

if __name__ == '__main__':
    unittest.main()
