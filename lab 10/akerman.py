def akerman(n, m):
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return akerman(n - 1, m)
    elif n > 0 and m > 0:
        return akerman(n - 1, akerman(n, m - 1))
print('Значение функции: ', Akkerman(n, m)
