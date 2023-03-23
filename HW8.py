# Напишите функцию для транспонирования матрицы


def transp_matrix(matrix: list):
    matrix1 = []
    matrix1_rows = zip(*matrix)
    for row in matrix1_rows:
        matrix1.append(list((row)))
    return matrix1


matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(transp_matrix(matrix))