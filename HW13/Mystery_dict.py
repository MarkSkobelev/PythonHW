"""Функция словарь, возвращает ключ и значение по введенному числу"""

__all__ = ['dict_myst']


def dict_myst(num: int):
    dictionary = {'Что было «Завтра», а будет «Вчера»?': 'сегодня',
                  'У него огромный рот, Он зовется … ?': 'бегемот',
                  'Маленькая печка с красными угольками.': 'гранат',
                  'Конь бежит, земля дрожит?': 'гром'}
    result = list(dictionary.items())[num-1]
    return result


if __name__ == '__main__':
    print(dict_myst(int(input("Введите номер загадки от 1 до 4: "))))