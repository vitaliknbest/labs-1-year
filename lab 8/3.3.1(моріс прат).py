import timeit
setup = '''
text = input('де шукаємо')
pat = input('що шукаємо')
d = [0]*len(pat)
j = 0
for i in range(1, len(pat)):
    while j > 0 and pat[i] != pat[j]:
        j = d[j - 1]
    if pat[i] == pat[j]:
        j +=1
    d[i] = j'''
stmt = '''for i in range(0, len(text)):
    while j > 0 and pat[j] != text[i]:
        j = d[j - 1]
    if pat[j] == text[i]:
        j += 1
    if j == len(pat):
        print('підстрока найдена в позиції', i - j + 1)
        j = d[ j - 1]'''
t =  timeit.timeit(stmt, setup, number = 1000 )
print('час за 1000 повторень алгоритму', t,\
      '\nкількість зрівнень у найгіршому разі = len(text) * len(pat)')
