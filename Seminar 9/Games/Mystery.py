from Mystery_dict import *

__all__ = ['mystery']


def mystery(num: int) -> str:
    user_number = dict_myst(int(input("Введите номер загадки от 1 до 4: ")))
    for i in range(num):
        print(user_number[0])
        answer = input("Ваш ответ: ").lower()
        if answer == user_number[1]:
            return "Верно!"
        else:
            num: int + 1
    return "У Вас закончились попытки!"


if __name__ == '__main__':
    print(mystery(int(input("Введите количество попыток: "))))