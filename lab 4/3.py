'''   виконав НАсадюк Віталій
написати програму яка визначає повну кількість годин  і повну кількість хвилин які пройшли до моменту даної секунди
'''
while True:
    try:
        d = 3600
        v = 60
        s = int(input("секунди ="))
        h = s // d
        m = (s - h * d) // v
        print("Години =", h, "Хвилини =", m)
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
