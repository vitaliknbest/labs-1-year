import numpy as np
import random

def summa(matrix):
    sum = 0
    for i in range(m):
        for j in range(m):
            matrix[i,j] = int(input('введіть елемент'))
            sum += matrix[i,j]
    return sum


def summa_rek(matrix):
   if len(matrix) == 1:
        return matrix[0]
   else:
        return matrix[0] + summa_rek(matrix[1:])


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
        return matrix[0] * mult_rec(matrix[1:])


def seach(matrix, a):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == a:
                return i+1, j+1


def seach_rec(matrix,a):
    if len(matrix) == 1:
        return matrix[0]
    else:
        i = 0
        j = 0
        if matrix[i][j] == a:
            return (i,j)
        else:
            seach_rec(matrix[i+1,j+1],a)


while True:
    try:
        m = int(input('введіть розмірність квадратної матриці'))
        choice = input("згенерувати матрицю (2) чи хочете ввести вручну(1)")
        if choice == '1':
            matrix = np.zeros((m, m), np.int)
            for i in range(m):
                for j in range(m):
                    matrix[i][j] = int(input('введіть елемент'))
        elif choice == '2':
            matrix = np.zeros((m, m), np.int)
            for i in range(m):
                for j in range(m):
                    matrix[i][j] = random.randint(1000,1000)
        else:
            raise ValueError
        a = int(input('введіть який елемент шукати'))
        print('сума елементів матриці ітераційно:{} рекурсивно{}:'.format(summa(matrix),summa_rek(matrix)))
        print('добуток елементів матриці ітераційно:{} рекурсивно{}:'.format(mult(matrix),mult_rec(matrix)))
        print('шуканий елемент матриці ітераційно:{} рекурсивно{}:'.format(seach(matrix,a),seach_rec(matrix,a)))
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
