"""Task 1 - Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы. Слова выводятся отсортированными согласно кодировки Unicode
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки"""
# import string
# string.punctuation
# def format_text(t1: str):
#     # Чистим пунктуацию и прочие символы в тексте
#     for i in string.punctuation:
#         if i in t1:
#             t1 = t1.replace(i, '')
#         t1 = t1.replace('—', '').strip()
#     t2 = sorted(t1.split())
#     max_len = len(max(t2, key=len))
#     for i, value in enumerate(t2, start=1):
#         print(f'{i} {value:>{max_len}}')
#     print('*' * 50)
#     print(max_len)
#
# format_text(text := input())

"""Task 2 - Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию."""
# def text_to_list(t1: str):
#     res = set()
#     for item in t1:
#         res.add(ord(item))
#     res = sorted(res, reverse=True)
#     return res
#
# print(text_to_list(text := input()))

"""Task 3 - Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно"""

#
# def two_num(n: str):
#     one, two = map(int, n.split())
#     my_dict = {}
#     for i in range(min(one, two), max(one, two) + 1):
#         my_dict[chr(i)] = i
#     return my_dict
#
#
# print(two_num(input()))

"""Task 4 - Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком. Её описание есть в википедии."""


# def sort_bubble(n: list):
#     a = 1
#     while a < len(n):
#         for i in range(len(n) - a):
#             if n[i] > n[i+1]:
#                 n[i], n[i+1] = n[i+1], n[i]
#         a += 1
#     return n
#
#
# print(sort_bubble(list(map(int, input().split()))))

"""Task 5 - Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида “10.25%”.
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


# def bonus(names: list, salaries: list, awards: list):
#     result = {}
#     for n, s, a in zip(names, salaries, awards):
#         result[n] = float(s * a)
#     return result
#
#
# names = ["Марк", "Андрей", "Иван", "Платон", "Мирон"]
# salaries = [100_000, 110_000, 50_000, 45_000, 47_000]
# awards = [0.1, 0.25, 0.13, 0.99, 0.98]
#
# print(bonus(names, salaries, awards))