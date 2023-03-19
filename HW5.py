# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list1 = [1, 2, 2, 3, 5, 6, 6, 8, 9, 25, 75, 25]
list2 = []
counter: int = 0
for item in list1:
    counter = list1.count(item)
    if counter > 1:
        if item not in list2:
            list2.append(item)
print(list2)
