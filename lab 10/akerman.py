#Насадюк Віталій КНІТ 16-а
#Вирахувати функцію Аккермана

def f(m,n):
    '''
    функція акермана

    :param m:перше число
    :param n: друге число
    :return: значення функції
    '''

    if m == 0:
        return ( n + 1 )
    if m > 0 and n == 0:
        return f(m-1, 1)
    if m > 0 and n > 0:
        return f(m-1, f(m, n-1))



def ackermann(m, n):
    """
    функція акермана ітераційно

    :param m:перше число
    :param n: друге число
    :return: значення функції
    """
    stack = []
    while True:
        if not m:
            if not stack:
                return n + 1
            m, n = stack.pop(), n + 1
        elif not n:
            m, n = m - 1, 1
        else:
            stack.append(m - 1)
            n -= 1

while True:
    try:
        n = int(input('n = '))
        m = int(input('m = '))
        с = 0
        print('Значення функції(рекурсивно): ', f(m, n), 'глибина рекурсії', с)
        print('(ітераційно) ', ackermann(m, n))
    except (ValueError, MemoryError, RecursionError):
        print("Введіть правельне значення/ занадто велике значення ")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break