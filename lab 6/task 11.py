#НАсадюк Віталій КНИТ16-А
#По дате d, m, y определить дату следующего дня
class date:
    days = range(1, 32)
    month = range(1, 13)
    years = range(1901, 2020)
while True:
    try:
        d,m,y = int(input('day :')),int(input('month :')),int(input('year :'))
        if d in range(1,32) and m in range(1,13) and y in range(1901,2020):
            if d + 1 not in date.days and m + 1 in date.month:
                print('1', '.', m+1, '.', y)
            elif d + 1 in date.days :
                print(d +1, '.', m, '.', y)
            else:
                print('1', '.', '1',  '.', y +1)
        else :
            print("Введіть коректні дані")
    except ValueError:
        print('Введіть коректні дані')
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
