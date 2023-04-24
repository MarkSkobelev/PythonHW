"""
Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- умножения матриц
"""
import random


class Matrix:

    def __init__(self, m: int):
        self.m = m
        a = []
        for i in range(self.m):
            a.append([0] * self.m)

        for i in range(self.m):
            for j in range(self.m):
                a[i][j] = random.randint(1, 10)
        self.m = a


    def __repr__(self) -> str:
        # Вывод на печать
        return f'Matrix: {self.m}'


    def __add__(self, other):
        # Сложение
        result = []
        numbers = []
        if len(self.m) != len(other.m[0]):
            return 'Матрицы разных размеров. Сложение невозможно'
        else:
            for i in range(len(self.m)):
                for j in range(len(self.m[0])):
                    res = self.m[i][j] + other.m[i][j]
                    numbers.append(res)
                    if len(numbers) == len(self.m):
                        result.append(numbers)
                        numbers = []
        return result


    def __mul__(self, other):
        # Умножение
        res = []
        num = []
        if len(self.m) != len(other.m[0]):
            return 'Матрицы не согласованы'
        else:
            for i in range(len(self.m)):

                for j in range(len(self.m[0])):
                    result = self.m[i][j] * other.m[i][j]
                    num.append(result)
                    if len(num) == len(self.m):
                        res.append(num)
                        num = []
        return res


martix_one = Matrix(5)
print(martix_one)
martix_two = Matrix(5)
print(martix_two)
print(martix_one == martix_two)  # Сравнение
print(martix_one + martix_two)
print(martix_one * martix_two)