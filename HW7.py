'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.'''

import random
backpack = {'Палатка': 3.0, 'Топор': 3.5, 'Термос': 1.0, 'Нож': 0.4, 'Спальник': 1.5, 'Котелок': 0.35, 'Аптечка': 1.0,
            'Компас': 0.2, 'Мультитул': 0.4}
max_load = int(input('Введите максимальную грузоподъемность вашего рюкзака в килограммах: '))

def backpack_list(d: dict):
    equip_list = []
    weight = 0
    d_copy = d.copy()
    while d_copy:
        random_equip = random.choice(list(d_copy.keys()))
        if weight + d_copy.get(random_equip) < max_load:
            equip_list.append(random_equip)
            weight += d_copy.get(random_equip)
            d_copy.pop(random_equip)
        else:
            d_copy.pop(random_equip)
            continue
    print(f'Максимальный вес вашего рюкзака {weight} кг\nСписок вашего снаряжения: ', equip_list)


backpack_list(backpack)



