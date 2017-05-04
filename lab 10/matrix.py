import numpy as np


m = int(input('введіть розмірність квадратної матриці'))
matrix = np.zeros((m,m), np.int)

sum = 0
for i in range(m):
    for j in range(m):
        matrix[i,j] = int(input('введіть елемент'))
        sum += matrix[i,j]
print(sum)
def sum (matrix):
    if len(matrix) == 0:
        return 0
    else:
        return sum(matrix[:-1]) + matrix[-1]


print(sum(matrix))
