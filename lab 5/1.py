""" виконав НАсадюк Віталій
написати програму яка в заданому не пустому тексті міняє 'ph' на 'f'
"""
while True:
    text = input()
    if text.isalpha():
        print(text.replace("ph", "f"))
    else:
        print("ви ввели не строку")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
