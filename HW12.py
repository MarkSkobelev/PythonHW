"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fib_numbers(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
        yield f1


print(*fib_numbers(int(input('Введите количество чисел Фибоначчи: '))))