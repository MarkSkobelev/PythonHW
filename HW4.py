# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение
# дробей. Для проверки своего кода используйте модуль fractions.

import fractions
import math
from math import gcd
a: str = str(input("Введите первую дробь вида a/b: "))
b: str = str(input("Введите вторую дробь вида a/b: "))
a1 = a.split('/')
b1 = b.split('/')
x1 = int(a1[0])
y1 = int(a1[1])
x2 = int(b1[0])
y2 = int(b1[1])
if y1 == y2:
    print('Сумма дробей:', '{}/{}'.format(x1 + x2, y1))
else:
    cd = int(y1 * y2 / gcd(y1, y2))
    rn = int(cd / y1 * x1 + cd / y2 * x2)
    print('Сумма дробей: ', '{}/{}'.format(rn, cd))

mult1 = (x1 * x2)
mult2 = (y1 * y2)
# print(x1, y1, x2, y2)
print('Произведение дробей: ' + str(mult1), str(mult2), sep='/')

f1 = fractions.Fraction(x1, y1)
f2 = fractions.Fraction(x2, y2)
print('Проверка суммы: ', f1 + f2)
print('Проверка произведения:', f1 * f2)