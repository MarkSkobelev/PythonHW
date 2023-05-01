import doctest
import unittest
import pytest


def duplicate_num(*args):
    """Создает новый список дубликатов без повторений"""
    list_1 = [*args]
    print(list_1)
    list_2 = []
    for item in list_1:
        if list_1.count(item) > 1 and item not in list_2:
            for i in range(list_1.count(item)):
                if item not in list_2:
                    list_2.append(item)
    return list_2


def test_positive():
    assert duplicate_num(0, 1, 3, 4, 4, 1, 6, 5, 2, 7, 2, 8, 7, 9) == [1, 4, 2, 7]


def test_no_args():
    assert duplicate_num() == []


def test_negative_args():
    assert duplicate_num(-1, -3, -2, -3, -4, -5) == [-3]


def test_letters():
    assert duplicate_num('a', 'v', 'a') == ['a']

def test_all():
    assert duplicate_num('a', 'v', 'a', 1, 2, 2, 4, 'В', 'о', 'В') == ['a', 2, 'В']

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    # unittest.main(verbosity=2)
    # pytest.main([-vv])