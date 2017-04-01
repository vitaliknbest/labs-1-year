import numpy as np

while True:
    do = input('введіть що ви хочете зробити з масивом)\n'
               '(повернути масив на 90 градусів за часовою стрілкою -- 1)\n'
               '(елементи лінійного масиву здвинути на к позицій -- 2)\n'
               '(знайти добуток двох квадратких матриць -- 3)\n'
               '(визначити детермінант матриці -- 4)\n')
    if do == '1':
        try:
            size = input('введіть розмірність матриці(зразок 3*3)\n').split('*')
            n, m = int(size[0]), int(size[1])
            matrixt = np.zeros((n, m), dtype=int)
            if n == m:
                for i in range(n):
                    for j in range(m):
                        matrixt[i, j] = int(input('a[' + str(i) + ']'
                                                                  '[' + str(j) + '] = '))
                i = 0
                n -= 1
                print('Матриця до повертання: \n', matrixt )
                for j in range(n):
                    matrixt[i + j][n], matrixt[n][n - j], matrixt[n - j][i], matrixt[i][j] = matrixt[i][j], matrixt[i + j][n], matrixt[n][n - j], matrixt[n - j][i]
                print('перевернута матриця: \n', matrixt)
            else:
                print('матриця повинна бути квадратною!!!')
        except (IndexError, ValueError):
            print('введіть коректні дані!')
    if do == '2':
        try:
            k = int(input('На скільки позицій ви хочете змістити? \n'))
            leght = int(input('скільки елементів має бути в масивові\n'))
            matrixt = np.zeros(leght,dtype=int)
            for j in range(leght):
                matrixt[j] = int(input('a[' + str(j) + ']' + '='))
            a = matrixt
            m = 0
            while k > len(a):
                k -= len(a)
            if k > 0:
                while k != 0:
                    i = len(a) - 1
                    m = a[i]
                    for i in range(len(a) - 1, 0, -1):
                        a[i] = a[i - 1]
                    a[0] = m
                    k -= 1
            else:
                while k != 0:
                    i = 0
                    m = a[i]
                    for i in range(len(a) - 1):
                        a[i] = a[i + 1]
                    a[len(a) - 1] = m
                    k += 1
           
            print(matrixt)
        except (IndexError, ValueError):
            print('введіть коректні дані!')
    if do == '3':
        try:
            size1 = input('введіть розмірність першої  матриці(зразок 3*3)\n').split('*')
            n1, m1 = int(size1[0]), int(size1[1])
            matrixt1 = np.zeros((n1, m1), dtype=int)
            c = np.zeros((n1, m1), dtype=int)
            if n1 == m1:
                for i in range(n1):
                    for j in range(m1):
                        matrixt1[i, j] = int(input('a[' + str(i) + ']'
                                                                   '[' + str(j) + '] = '))
            else:
                print('матриці повинні бути квадратними!!!')
            size2 = input('введіть розмірність другої матриці(зразок 3*3)\n').split('*')
            n2, m2 = int(size2[0]), int(size2[1])
            matrixt2 = np.zeros((n2, m2), dtype=int)
            if n2 == m2:
                for i in range(n2):
                    for j in range(m2):
                        matrixt2[i, j] = int(input('a[' + str(i) + ']'
                                                                   '[' + str(j) + '] = '))
            else:
                print('матриці повинні бути квадратними!!!')
            if m1 == n2:
             for i in range(n1):
                for j in range(n1):
                    for k in range(n1):
                        c[i][j] += matrixt1[i][k] * matrixt2[k][j]
            print('Произведение матриц: \n', c)
        except(IndexError, ValueError):
            print('введіть коректні дані')
    if do == '4':
        try:
            size = input('введіть розмірність матриці(зразок 3*3)\n').split('*')
            n, m = int(size[0]), int(size[1])
            matrixt = np.zeros((n, m), dtype=int)
            if n == m:
                for i in range(n):
                    for j in range(m):
                        matrixt[i, j] = int(input('a[' + str(i) + ']'
                                                                  '[' + str(j) + '] = '))
                w = 0
                det = 1
                while w != n - 1:
                    d = matrixt[w, w]
                    det *= d 
                    for i in range(w + 1, n):
                        vit = matrixt[i][w] / d  
                        for j in range(n):
                            matrixt[i, j] -= vit * matrixt[w][j]
                    w += 1
                print('Определитель матрицы = ', '%.0f' % (det * matrixt[w][w]))
            else:
                print('матриця повинна бути квадратною!!!')
            
           
        except (IndexError, ValueError):
            print('введіть коректні дані!')
    while True:
        out = input("Бажаєте продовжити ?(y /n )\n")
        if out == "y" or out == "n":
            break
        print('Не коректні данні!')
    if out == "y":
        continue
    if out == "n":
        break
