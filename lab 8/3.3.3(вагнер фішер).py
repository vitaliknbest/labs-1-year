from timeit import timeit
setup = '''
text = input('де шукаємо: ')
pat = input('що шукати: ')
m = len(text)
n = len(pat)
d = [[0 for i in range(n + 1)] for j in range(m + 1)]
'''
stmt = '''
for i in range(m + 1):
    d[i][0] = i
for j in range(n + 1):
    d[0][j] = j
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if text[i - 1] == pat[j - 1]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = 1 + min(d[i - 1][j], d[i - 1][j - 1], d[i][j - 1])
print(d[i][j])            
'''

print('час за виконання 1000 повторень', timeit(stmt, setup, number=100))
