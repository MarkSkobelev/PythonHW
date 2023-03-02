print('Введите стороны треугольника: A, B, C. Нажимайте Enter после каждого ввода числа')
a, b, c = int(input()), int(input()), int(input())
if (a < b + c) and (b < c + a) and (c < a + b):
    if (a == b != c) or (b == c != a) or (c == a != b):
        print('Это равнобедренный треугольник')
    elif (a == b == c):
        print('Это равносторонний треугольник')
    else:
        print('Это разносторонний треугольник')
else:
    print('Это не треугольник!')
