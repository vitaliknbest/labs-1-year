sign = "+-=*"
digit = '0987654321'


def formula(text):
    for i in text:
        if i not in sign and i not in digit:
            raise ValueError
    text = text.split('=')
    for i in text:
        if len(text) > 1:
            formula(i)
            return True
        else:
            return False


while True:
    try:
        text = input('введіть формулу')
        print(formula(text))
    except ValueError:
        print("Введіть правельне значення/гадто велике число")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
