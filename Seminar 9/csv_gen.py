import csv
import random
def csv_gen():
    """Генерация csv файла с 3 случайными числами"""
    numbers = []
    for i in range(random.randint(10, 100)):
        n = []
        numbers.append(n)
        for _ in range(3):
            l: int = random.randint(1, 999)
            n.append(str(l))
    with open('3_numb.csv', 'w', newline='', encoding='utf-8') as file:
        csv_write = csv.writer(file)
        for row in numbers:
            csv_write.writerow(row)

if __name__ == '__main__':
    csv_gen()