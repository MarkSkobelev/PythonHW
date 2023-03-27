# a, b, c = ('один', 'два', 'три',)
# print(f'{a=} {b=} {c=}')
#
# data = ['один', 'два', 'три', 'четыре', 'пять']
#
# print(*data, sep=' * ')
#
# t = 1, 2, 3
# print(f'{t=}, {type(t)}')
#
# data = {10, 9, 8, 2, 1, 5}
# a, b, c, *d, e = data
# print(a, b, c, d, e)

# data = (10, 9, 8, 2, 1, 5)
# list_iter = iter(data)
# a, b, c = next(list_iter), next(list_iter), next(list_iter)
# print(a, b, c)
# print(type(b))

# data = {'один': 1, 'два': 2, 'три': 3}
# x = iter(data.items())
# print(x, type(x))
# y = next(x)
# print(y)
# z = iter(y)
# a, b = next(z), next(z)
# print(a, type(a), b, type(b))

"""Task 1 - Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь, где:
второе и третье число являются ключами
первое число является значением для первого ключа
четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа"""


# def slash(s: str):
#     one, two, three, *other = s.split('/')
#     result = {int(two): int(one), int(three): tuple(map(int, other))}
#     return result
# print(slash(input("Введите числа через "/": ")))


"""Task 2 - Самостоятельно сохраните в переменной строку текста.
Создайте из строки словарь, где ключ - буква, а значение - код буквы.
Напишите преобразование в одну строку."""

# str1 = "Hello world!"
# res_dict = {key: ord(key) for key in str1}
# print(res_dict)
#
# res = {}
# for key in str1:
#     res[key] = ord(key)
# print(res)

"""Task 3 - Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили. Сохраните его итератор.
Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю."""

# str1 = "Hello world!"
# res_dict = {key: ord(key) for key in str1}
# x = iter(res_dict.items())
# for i in range(5):
#     print(next(x))

"""Task 4 - Создайте генератор чётных чисел от нуля до 100.
Из последовательности исключите числа, сумма цифр которых равна 8.
Решение в одну строку."""

# gen_chet = (i for i in range(0, 101, 2) if (i // 10) + (i % 10) != 8)
# print(*gen_chet)

"""Task 5 - Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»."""
# my_list = []
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         my_list.append('FizzBuzz')
#     elif i % 3 == 0:
#         my_list.append("Fizz")
#     elif i % 5 == 0:
#         my_list.append("Buzz")
#     else:
#         my_list.append(i)
# print(my_list)


# my_list2 = ("FizzBuzz" if (i % 3 == 0 and i % 5 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else i for i in range(1, 101))
# print(*my_list2)

"""Task 6 - Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - отдельный пример таблицы умножения.
Для вывода результата используйте “принт” без перехода на новую строку."""


"""Task 7 - Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: “число является простым, 
если делится нацело только на единицу и на себя”."""

# def gen_num(num: int):
#     for i in range(2, num + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             yield i
# print(*gen_num(int(input("Введите число: "))))


