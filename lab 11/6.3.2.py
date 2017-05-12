import pickle
import numpy as np
import os

os.chdir('D:/NewFold/')


def Dijkstra(N, S, matrix):
    valid = [True] * N
    weight = [1000000] * N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


while True:
    try:
        N = int(input("введіть кількість міст: "))
        matrix = np.ones((N, N), dtype=int)
        matrix = matrix * (-1)
        a = []
        for i in range(N):
            a.append(input("Введіть назву міста :  "))
        for i in range(N):
            for j in range(N):
                if i != j:
                    if matrix[i][j] == -1 and matrix[j][i] == -1:
                        matrix[i][j] = matrix[j][i] = int(
                            input("довжина між містами " + a[i] + " і " + a[j] + ": "))
                else:
                    matrix[i][j] = 0
        print(Dijkstra(N, 0, matrix))

    except ValueError:
        print("Введіть правельне значення")
        filee = open("out.bin", 'wb')
        pickle.dump(matrix, filee)
        filee.flush()
        filee.close()
        filee = open('out.bin', 'rb')
        filee.read()
        result.close()

    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
