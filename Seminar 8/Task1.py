"""
Task 1 - Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json

__all__ = ['convert']
def convert(file_name:str)-> None:
    dic = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            list_f = line.split(',')
            dic[list_f[0].capitalize()] = float(list_f[1])
        #print(dic)
    with open('file_json.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)# indent=2 - перенос на новую строку
convert('union_data.txt')
