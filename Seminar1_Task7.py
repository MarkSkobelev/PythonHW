"""
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""
MIN_NUMBER = 1
MAX_NUMBER = 999
number = 0
while (number < 1 or number > 1000):
    number = int(input(f"Введите число от {MIN_NUMBER} до {MAX_NUMBER}\n"))
if (number < 10):
    result = number **2
elif (10 <= number <= 99):
    result = (number // 10) * (number % 10)
elif (100 <= number <= 999):
    result = (number % 10) * 100 + ((number % 100) // 10) * 10 + (number // 100)
print(result)