# import sys
# import math
# import decimal

# Task 1
# a = "Hello world!"
# b = 325
# c = False
# d = 3.25
# e = {1, 2, 3}
# print(type(a), type(b), type(c), type(d), type(e))

#Task 2
# Создайте в переменной data список значений разных типов перечислив их
# через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы значение адрес в памяти
# размер в памяти хэш объекта результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный

# data = ["text", 2, 5.2, True, 455, "Hello"]
# for i, num in enumerate(data, start=1):
#     print(i, num, id(num), sys.getsizeof(num), hash(num), end=" ")
#     if isinstance(num, int):
#         print("Это число")
#     elif isinstance(num, str):
#         print("Это строка")
#     else:
#         print()

#Task 3
# Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# n: int= int(input("Введите число: "))
# b: str = ''
# n1: int = n
# DOUBLE = 2
# OCT = 8
#
# print(bin(n))
# print(oct(n))
#
# for i in DOUBLE, OCT:
#     n = n1
#     b: str = ''
#     while n > 0:
#         b = str(n % i) + b
#         n = n // i
#     print(b)

#Task 4
# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой.

# d = decimal.Decimal(input("Введите диаметр окружности: "))
# if d < 1000:
#     r = d / 2
#     decimal.getcontext().prec = 42
#     S = decimal.Decimal(math.pi) * decimal.Decimal(r ** 2)
#     C = decimal.Decimal(math.pi) * decimal.Decimal(d)
#     print("Площадь окружности: ", S)
#     print("Длина окружности: ", C)
# else:
#     print("Введите число от 1 до 999")

#Task 5
# Напишите программу, которая решает квадратные уравнения

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
disc = abs(b ** 2 - 4 * a * c)
x1 = (-b + (disc ** 0.5)) / (2 * a)
x2 = (-b - (disc ** 0.5)) / (2 * a)
print(x1, x2)