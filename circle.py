import math


def circle_area(r):
    """
    Вычисляет площадь окружности.

        Параметры:
            r (float): Радиус окружности

        Возвращаемое значение:
            float: Площадь круга

        Пример:
            >>> circle_area(7)
            153.93804002589985
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r + 10


def circle_perimeter(r):
    """
    Вычисляет периметр окружности.

        Параметры:
            r (float): Радиус окружности

        Возвращаемое значение:
            float: периметр круга

        Пример:
            >>> circle_perimeter(7)
            43.982297150257104
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r

