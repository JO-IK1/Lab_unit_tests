import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    """Тесты для функций, связанных с кругом."""

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        # округляем результат до 2 знаков после запятой
        self.assertAlmostEqual(area(3), math.pi * 9, places=6)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2, places=6)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-3)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == '__main__':
    unittest.main()
