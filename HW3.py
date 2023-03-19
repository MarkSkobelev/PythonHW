# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input("Введите число: "))
num1 = num
result = ''
while num > 0:
    ost = num % 16
    if ost == 10:
        str16 = 'a'
    elif ost == 11:
        str16 = 'b'
    elif ost == 12:
        str16 = 'c'
    elif ost == 13:
        str16 = 'd'
    elif ost == 14:
        str16 = 'e'
    elif ost == 15:
        str16 = 'f'
    else:
        str16 = str(ost)
    result = str16 + result
    num //= 16
print('Число в шестнадцатиричной системе счисления: ', result)
print('Проверка через hex', hex(num1))