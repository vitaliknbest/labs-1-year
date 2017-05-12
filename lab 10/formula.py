#Насадюк Віталій КНІТ 16-а
# Вирахувати суму елементів матриці
#Нписати програму яка визначає чи заданий текст є формулою чи ні#


sign = "+-* "
digit = '0987654321'

def itera(text):
    '''
    функція перевіряє чи даний текст є формулою ітераційно

    :param text: текст який треба перевірити
    :return: True або False
    '''
    if text.endswith('.'):
        text = text.split('.')
        text = ''.join(text)
        text = text.split('=')
        text = ''.join(text)
        text = text.split(sign)
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
    else:
        return False

def formula(text):
    '''
    функція перевіряє чи даний текст є формулою рекурсивно
    :param text: текст який треба перевірити
    :return: True або False
    '''

    if text.endswith('.'):
        text = text.split('.')
        text = ''.join(text)
        text = text.split('=')
        text = ''.join(text)
        text = text.split(sign)
        for i in text:
            if i == '':
                return False
            for j in i:
                if j not in sign and j not in digit:
                    raise ValueError
        for i in text:
            if len(text) >= 1:
                formula(i)
                return True
            else:
                return False
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
