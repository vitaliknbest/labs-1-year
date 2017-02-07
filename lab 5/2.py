
'''виконав Насадюк Віталій
написати програму яка переводить число з 8 системи зчислення в 5 систему зчислення

'''

while True:
    try:
        def oxttofixt(x):
            n = ""
            while x > 0:
                y = str(x % 5)
                n = y + n
                x //= 5
            return n

        x = int(input(), 8)
        print(oxttofixt(x))

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
