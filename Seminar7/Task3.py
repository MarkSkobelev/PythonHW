"""
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""
__all__ = ['union']

def union(a: str, b: str):
    with open(a, 'r', encoding='utf-8') as f1, \
            open(b, 'r', encoding='utf-8') as f2, \
                open('union_data.txt', 'w', encoding='utf-8') as f3:
            lenf1 = sum(1 for i in f1)
            lenf2 = sum(1 for i in f2)
            print(lenf1, lenf2)
            for i in range(max(lenf1, lenf2)):
                text = f1.readline()
                if text == "":
                    f1.seek(0)
                    text = f1.readline()
                text = text[:-1] #убираем последний символ
                num = f2.readline()
                if num == "":
                    f2.seek(0)
                    num = f2.readline()
                    num = num.replace(" ", "")[:-1]
                    num1, num2 = num.split('|')
                res_mult = int(num1) * float(num2)
                if res_mult < 0:
                    f3.write(f'{text.lower()},{abs(res_mult)}\n')
                else:
                    f3.write(f'{text.upper()},{round(res_mult)}\n')


if __name__ == '__main__':
    union('data2.txt', 'data1.txt')
