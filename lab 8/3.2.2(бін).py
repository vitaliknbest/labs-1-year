import timeit
setup = '''
import numpy as np
n = int(input('скільки елементів'))
a = np.arange(n)
x = int(input('яке число найти (від 1 до' + str(n) + ')'))
flag = False
L = 0
R = len(a) - 1
k = 0
'''
stmt = '''while L <= R and not flag:
    k = (L + R) // 2'''
'''    if x < a[k]:
        R = k - 1
    elif x > a[k]:
        L = k + 1
    else:
        x = k 
       break
if x == k:
    print('Елемент знайдений в позиції'.format(x, k))
else:
    print('Елемент не знайдено!')'''
print(timeit.timeit(stmt, setup, number= 1000))
print(' в найгіршому разі алгоритм потребує n+1//2 зрівнень')
