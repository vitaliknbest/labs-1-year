while True:
    try:
        s = input("введіть послідовність цілих чисел через кому\n")
        for i in s:
            if i == ',' or int(i)== 0-9:
                s = str(s)
                s = s.split(',')
        print(len(set(s)))
    except ValueError:
        print('Введіть числа через кому')
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
