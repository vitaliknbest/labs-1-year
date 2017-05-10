import numpy as np
import random


def summa(matrix):
    sum = 0
    for i in range(m):
        for j in range(m):
            sum += matrix[i, j]
    return sum


def summa_rec(matrix):
    if len(matrix) == 1:
        return matrix[0]
    else:
        summ = sum((matrix[0] + summa_rec(matrix[1:])))
        return summ


def mult(matrix):
    n = 1
    for i in matrix:
        for j in i:
            n *= j
    return n


def mult_rec(matrix):
    if len(matrix) == 1:
        return matrix[0]
    else:
        prodd = np.array([(matrix[0] * mult_rec(matrix[1:]))])
        prodd = prodd.prod()
        return prodd


def seach(matrix, a):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == a:
                return i, j


def seach_rec(i, j, a, matrix):

    if matrix[i][j] == a:

        return i, j
    else:
        global c1, c2
        c1, c2 = i, j
        if j + 1 < len(matrix[0]):
            seach_rec(i, j + 1, a, matrix)
        if i + 1 < len(matrix[1]):
            seach_rec(i + 1, 0, a, matrix)


while True:
    try:
        m = int(input('введіть розмірність квадратної матриці'))
        choice = int(input("згенерувати матрицю (2) чи хочете ввести вручну(1)"))
        a = int(input('введіть який елемент шукати'))
        c1 = 0
        c2 = 0

        if choice == 1:
            matrix = np.zeros((m, m), np.int)
            for i in range(m):
                for j in range(m):
                    matrix[i][j] = int(input('введіть елемент'))
        if choice == 2:
            matrix = np.zeros((m, m), np.int)
            for i in range(m):
                for j in range(m):
                    matrix[i][j] = random.randint(-100, 100)
        print(matrix)
        print('сума елементів матриці ітераційно: {} рекурсивно : {}'.format(summa(matrix), summa_rec(matrix)))
        print('добуток елементів матриці ітераційно: {} рекурсивно : {}'.format(mult(matrix), mult_rec(matrix)))
        print('шуканий елемент матриці ітераційно: {} рекурсивно : {}'.format(seach(matrix, a), seach_rec(i, j, a, matrix)))
    except (ValueError, MemoryError):
        print("Введіть правельне значення/ надто велике число")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
