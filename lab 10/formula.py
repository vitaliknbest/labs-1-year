sign = "+-* "
digit = '0987654321'

def itera(text):
    text = text.split('=')
    for i in text:
        if i.isdigit():
            return True
        else:
            return False
        i = i.split(sign)
        if i == '':
            return False
        else:
            return True

def formula(text):
    text = text.split('=')
    for i in text:
        if i == '':
            return False
        for j in i:
            if j not in sign and j not in digit:
                raise ValueError
    for i in text:
        if len(text) > 1:
            formula(i)
            return True
        else:
            return False


while True:
    try:
        text = input('введіть формулу ')
        print('рекурсія', formula(text))
        print("ітерація", itera(text))
    except ValueError:
        print("Введіть правельне значення/надто велике число")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
