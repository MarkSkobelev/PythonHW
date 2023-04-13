import random as rnd
from sys import argv

__all__ = ['guess']


def guess(down:int = 0, up:int = 100, chance:int = 5):
    number = rnd.randint(down, up)
    for i in range(chance):
        print(f'Введите число от {down} до {up}')
        num = int(input())
        if num > number:
            print('Меньше')
        elif num < number:
            print('Больше')
        else:
            return True
    return False

if __name__ == '__main__':
    tmp_path, *params = argv
    print(guess(*(int(n) for n in params)))