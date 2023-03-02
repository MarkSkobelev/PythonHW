"""
Напишите код, который запрашивает число и сообщает является ли оно простым
или составным. Используйте правило для проверки: “Число является простым,
если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
max_number = 100000
print("Введите число от 0 до 1000:")
number = int(input())
if number < 0 or number > max_number:
    print("Введите число от 0 до 1000!")
elif number == 0:
        print('0 не является простым числом')
elif number == 1:
        print('1 не является ни простым, ни составным числом, так как у него только один делитель — 1')
else:
    PrimeNumber = True
    for i in range(2, (number//2)+1):
        if number % i == 0:
            PrimeNumber = False
            break
    if PrimeNumber == False:
        print(f'{number} это составное число')
    else:
        print(f'{number} это простое число')