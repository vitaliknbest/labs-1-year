''' виконав Насадюк Віталій
написати програму яка присвоює перемінні d першу цифру після крапки числа х
'''
while True:
    try:
        x = float(input("Введіть дробове число:"))
        d = int(x * 10 % 10)
        print(d)
    except ValueError:
        print("Ведіть коректні дані")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
