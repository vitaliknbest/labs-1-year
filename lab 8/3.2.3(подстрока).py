import timeit
setup = '''
text = input('введіть текст в якому шукати')
pat  = input('введіть що шукати')
i = -1
j = 0'''
stmt = '''while (j < len(pat)) and (i < (len(text) - len(pat))):
    j = 0
    i += 1
    while j < len(pat) and pat[j] == text[i + j]:
        j +=1'''
t = timeit.timeit(stmt, setup, number= 1000)
print('час за 1000 повторень алгоритму', t,\
      '\nкількість зрівнень у найгіршому разі = len(text) + len(pat)')
#if j == len(pat):
#    print('підстрока знайдена в позиції', i)
#else:
#    print('строка не найдена')
