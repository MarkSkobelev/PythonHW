""" 1.Написать функции:
-Нахождение корней квадратного уравнения
-Генерации csv файла с 3 случайными числами в каждой строке 100-1000 строк
-Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждойй тройкой чисел из csv файла
-Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
"""
from cmath import sqrt
import csv
from typing import Callable
import json

__all__ = ['deco_1', 'deco_2', 'random', 'quadratic_equation']


def deco_1(func: Callable):
    """Чтение данных из csv файла, обработка данных"""
    def wrapper():
        with open('3_numb.csv', 'r', newline='', encoding='utf-8') as file:
            a = csv.reader(file)
            result = []
            for rows in a:
                [a, b, c] = int(rows[0]), int(rows[1]), int(rows[2])
                result.append(f'[{a},{b},{c}]:{func(a, b, c)}')
            return result
    return wrapper


def deco_2(func: Callable):
    """Запись результатов работы функции в json"""
    def wrapper():
        result = func()
        with open('3_numb.json', 'w') as f:
            json.dump(result, f, indent=2)
    return wrapper

@deco_2
@deco_1
def quadratic_equation(a: int, b: int, c: int) -> int:
    """Нахождение корней квадратного уравнения """
    if a == 0:
        return "Это не квадратное уравнение"
    d = b ** 2 - 4 * a * c
    x1 = (- b + sqrt(d)) / (2 * a)
    x2 = (- b - sqrt(d)) / (2 * a)
    d = [f'{x1}, {x2}']
    return d


quadratic_equation()