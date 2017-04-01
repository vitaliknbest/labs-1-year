import timeit
setup = '''
text = input('введіть текст в якому шукати')
pat = input('введіть що шукати')
n = len(text)
m = len(pat)
d = (m * (ord(max(max(text), max(pat))) + 1))
for i in range(m - 1):
    d[ord(pat[i])] = m - i - 1
pos = -1
i = 0
'''
stmt = '''
while n - i >= m and pos == -1:
    j = m - 1
    while text[i + j] == pat[j]:
        if j == 0:
            pos = i
            break
        j = -1
    i += d[ord(text[i + m - 1])]'''
'''
if pos != -1:
    print('підстрока найдена в похиції', pos)
else:
    print('елемант не знайдений')'''
print(timeit.timeit(stmt,setup,number= 1000))
print('в найгіршому випадку потребує m + n зрівнень')


