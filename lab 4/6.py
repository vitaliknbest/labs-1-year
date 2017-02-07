'''  виконав Насадюк Віталій
написати програму яка визначає значння перемінної number від 1 до 7 в залежності від того на який день тижня приходиться десь невисокосного року
'''
l = ["Неділя", "Понеділок", "Вівторок", "Середа", "Четвер", "Пятниця", "Субота"]
while True:
    while True:
        try:
            day = int(input('Введіть день :'))
            number = day % 7
            if day in range(1, 365):
                print(l[day % 7])
                break
            else:
                print("Введіть значення від  1 до 365!!!!")
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
