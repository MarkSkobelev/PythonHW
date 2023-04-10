"""
Task 2 - Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json

__all__ = ['ident']

def ident(name_file: str):
    dic = {}
    dic2 = {}
    with open(name_file, 'r', encoding='utf-8') as f:#чтение файла
        data = json.load(f)#запись данных в файл
    dic = data
    print(type(dic))
    print(dic)

    while True:
        name = input("Введите имя: ")
        if name == '':
            break
        id = int(input('Введите id: '))
        lev = input('Введите уровень доступа (от 1 до 7): ')
        dic2 = {id:name}

        if dic.get(lev) is None:
            dic[lev] = dic2# ключ: уровень доступа - значение словарь(id/Имя)
        else:
            k = dic.get(lev)
            k.update(dic2)

    with open(name_file, 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)

ident('ident.json')