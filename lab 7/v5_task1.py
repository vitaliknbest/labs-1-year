#  Насадюк Віталій
#  Вывести кол-во чисел, которые входят в последовательность боле одного раза
while True:
    try:
        s = input("введіть послідовність цілих чисел через кому\n").split(',')
        se = set()
        for i in s:
            if i.isdigit() and s.count(i) > 1:            
                se.add(i)
            else:
                raise ValueError
        print(len(se))
    except ValueError:
        print('Введіть числа через кому')
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        else:

            print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
        
