import unittest
import math
from circle import circle_area, circle_perimeter


class TestCircle(unittest.TestCase):
    """Тесты для функций, связанных с кругом."""

    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_circle_area_positive(self):
        # округляем результат до 2 знаков после запятой
        self.assertAlmostEqual(circle_area(3), math.pi * 9, places=6)

    def test_circle_perimeter_positive(self):
        self.assertAlmostEqual(circle_perimeter(2), 2 * math.pi * 2, places=6)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-3)

    def test_circle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-5)


if __name__ == '__main__':
    unittest.main()
