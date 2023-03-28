"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

def path_to_file(path: str):
    p1 = path.split('\\')
    p2 = p1[-1].split('.')
    tuple = '\\'.join(p1[:-1]), p2[0], p2[1]
    return tuple


print(path_to_file("С:\Пользователь\Desktop\GB\PYTHON_23\PythonHW\README.md"))