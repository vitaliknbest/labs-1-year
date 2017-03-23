import  enum
n = int(input('скільки товарів всього'))
name_tov = [''] * n
country = [''] * n
count = [0] * n
for i  in range(n):
    name_tov[i] = input('введіть назву товару')
    country[i]  = input('введіть назву країни')
    count[i]  = input('введіть кількість товару')
for i in range(n - 1):
    for j in range(i + 1, n):
         if name_tov[i] > name_tov[j]:
             name_tov[i],name_tov[j] =  name_tov[j],name_tov[i]
             country[i],country[j] =  country[j],country[i]
             count[i],count[j] =  count[j],count[i]
for i in range(n):
    print( name_tov[i], country[i],  count[i])