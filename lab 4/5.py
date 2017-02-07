''' виконав Насадюк Віталій
написати програму яка визначає повну кількість годин  і повну кількість хвилин і секунд
які пройшли від початку доби до того моменту коли часова стрілка повернулась на corner градусів  при чому corner дробове число
'''
a = 30
b = 0.5
c = 0.0083333333333333
while True:
    try:
        corent = float(input("Введіть кут :"))
        hours = corent // a
        minutes = (corent - a * hours) // b
        seconds = (corent - a * hours - b * minutes) // c
        print("Години:", hours, "Хвилини:", minutes, "Секунди:", seconds)
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
