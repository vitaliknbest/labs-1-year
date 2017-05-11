def nsd (a, b):
    '''
    визначає найбільший спільний дільник(рекурсивно)

    :param a: перше число
    :param b: друге число
    :return: найбільший спільний дільник
    '''
    return abs(a) if b == 0 else nsd(b, a % b)


while True:
    try:
        b = int(input('введіть перше число'))
        a = int(input('введіть друге  число'))
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

        print('ітераційно', a+b)
        print('рекурсивно',nsd(a,b))

    except (ValueError, MemoryError):
        print("Введіть правельне значення/ надто велике число")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break

