def num (n,):
    '''
    визначає скільки  є можливих  представлень числа n рекурсивно

    :param n: число  для якого треба визначити кількість представлення
    :return: повертає кількість представлень числа n
    '''
    c = 0
    a = n - 1
    while a > n // 2:
        b = n - a
        c = c + 1 + num(b)
        a -= 1
    return c

def iter(c):
    """
    визначає скільки  є можливих  представлень числа n ітераційно

    :param n: число  для якого треба визначити кількість представлення
    :return: повертає кількість представлень числа n
    """
    a = c - 1
    return len(list(enumerate(range(a, c // 2 - (c - a), -1))))

while True:
    try:
        n =  int(input('введіть число'))
        choice = int(input('порахувати рекурсивно(1) чи ітераційно(2)'))
        if choice == 1:
            print('рекурсія',num(n))
        elif choice == 2:
            print('ітерація',iter(n))
        else:
            print("введіть правельне значення")
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

