import numpy as np
matrix = []
y = 0
a = 0
fieldOrder = 0
detInverse = 0

def get_minor(column, matrix):
    minor = []
    for i in range(1, len(matrix)):
        row = []
        for j in range(len(matrix)):
            if not j == column:
                row.append(matrix[i][j])
        minor.append(row)
    return minor


def get_det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    det = 0
    mutiplier = 1
    for i in range(len(matrix)):
        el = matrix[0][i]
        if not el == 0:
            det += mutiplier * el * get_det(get_minor(i, matrix))
        mutiplier *= -1
    return det


def get_extended(x, y):
    global detInverse
    global a
    global fieldOrder
    if a == 0:
        x = 0
        y = 1
        return
    y_1 = 0
    x_1 = 0
    fieldOrder = a
    a = b % a
    get_extended(detInverse, y_1)
    x = y_1 - (b / a) * x_1
    y = x_1
    return


def get_minor_extended(matrix, row, column):
    minor = []
    for i in range(len(matrix)):
        if i == row:
            continue
        row = []
        for j in range(len(matrix)):
            if j == column:
                continue
            row.append(matrix[i][j])
        minor.append(row)
    return minor


def get_con_matrix(matrix):
    sign = 1
    flag = len(matrix) % 2 == 0
    con_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            con_matrix[i][j] = sign * get_det(get_minor_extended(matrix, i, j))
            sign *= -1
        sign *= -1 if flag else 1
    return con_matrix.T


def reduce_matrix(fieldOrder, detInverse):
    global matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] *= detInverse
            matrix[i][j] %= fieldOrder
            if matrix[i][j] < 0:
                matrix[i][j] += fieldOrder


def main():
    fieldOrder = int(input('Введите значение поля: '))
    n, m = input('Введите размерность матрицы: ').split()
    n, m = int(n), int(m)
    print('Введите элементы матрцы построчно: ')
    global matrix

    matrix = [[int(val) for val in input().split()] for i in range(n)]
    check = 0
    a = get_det(matrix)
    if a == 0:
        print('Определитель матрицы равен нулю')
    else:
        while a < 0:
            a += fieldOrder
        get_extended(x, y)


if __name__ == "__main__":
    main()