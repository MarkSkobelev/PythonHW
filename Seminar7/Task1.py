"""Task 1 - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции."""
import random as rnd

__all__ = ['fill_digits']

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def fill_digits(line:int, file_name:str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(line):
            tmp_str = str(rnd.randint(MIN_LIMIT, MAX_LIMIT)) + "|" + str(rnd.uniform(MIN_LIMIT, MAX_LIMIT))
            print(tmp_str)
            f.write(f'{tmp_str}\n')

if __name__ == '__main__':
    fill_digits(5, "data1.txt")

