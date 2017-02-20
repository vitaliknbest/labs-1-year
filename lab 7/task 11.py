n = 10
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s_1 = {i for i in range(n)}
s_2 = {i for i in range(n)}
suma = 0
for i in s_1:
    for j in s_2:
        if i in range(len(a)) and j in range(len(a[i])):
            suma += a[i][j]
print(suma)

