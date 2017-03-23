import timeit

setup = '''
import numpy as np
import random

n = int(input('скільки елементів'))
a = np.zeros(n, dtype=np.int)
for i in range(n):
    a[i] = random.randint(-128, 127)
x = int(input('яке число найти (від -127 до 127)'))
N = len(a)
i = 0
'''
stmt = 'while (i < N) and (a[i] != x): i += 1'
print(timeit.timeit(stmt, setup, number=100000))
print('в найгіршому разі алгоритм виконує n(кількість елементів) зрівнень')
# if i == N:
#   print('елемент не найден')
# else:
#    print('елемент', x,  "найден в позиції", i)
