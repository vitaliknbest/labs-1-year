''' роботу виконав студент першого курсу Насадюк Віталій Михайлович
Написати програму, яка міняє значення двох перемінниз без використання третьої перемінної
'''
while True:
    try:
        x = int(input("x = "))
        y = int(input("y = "))
        x, y = y, x
        print(" x = ", x, "y = ", y)
    except ValueError:
        print("Введіть правельне значення")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
