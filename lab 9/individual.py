import random
import numpy as np


def bubblesort(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

    приймає три параметри:
    1 масив
    2 кількість зрівнень
    3 кількість перестановок
    повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    for i in range(1, n + 1):
        for j in range(n - 1, i - 1, -1):
            comparison += 1
            if (mass[j - 1] < mass[j]):
                mass[j], mass[j - 1] = mass[j - 1], mass[j]
                exchange += 1
    return('зміни'), exchange, ('зрівнення'), comparison, mass


def insertionsort(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    for i in range(1, n):
        j = i - 1
        key = mass[i]
        while j >= 0 and mass[j] > key:
            comparison += 1
            mass[j + 1] = mass[j]
            j -= 1
            mass[j + 1] = key
            exchange += 1
    return ('зміни'), exchange, ('зрівнення'), comparison, mass

def selectionsort(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            comparison += 1
            if mass[j] < mass[min]:
                min = j
            mass[i], mass[min] = mass[min], mass[i]
            exchange += 1


def cocktailsort(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    for k in range(len(mass)-1, 0, -1):
        swapped = False
        for i in range(k, 0, -1):
            comparison += 1
            if mass[i]<mass[i-1]:
                mass[i], mass[i-1] = mass[i-1], mass[i]
                exchange += 1
                swapped = True

        for i in range(k):
            comparison += 1
            if mass[i] > mass[i+1]:
                mass[i], mass[i+1] = mass[i+1], mass[i]
                exchange += 1
                swapped = True
      
        if not swapped:
            return ('зміни'), exchange, ('зрівнення'), comparison, mass


def heapsort(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    def heapify(mass):
        start = (len(mass) - 2) // 2
        while start >= 0:
            siftDown(mass, start, len(mass) - 1)
            start -= 1

    def siftDown(mass, start, end):
        root = start
        while root * 2 + 1 <= end:
            nonlocal comparison
            comparison += 1
            child = root * 2 + 1
            if child + 1 <= end and mass[child] < mass[child + 1]:
                child += 1
            if child <= end and mass[root] < mass[child]:
                mass[root], mass[child] = mass[child], mass[root]
                nonlocal exchange
                exchange += 1
                root = child
            else:
                return

    heapify(mass)
    end = len(mass) - 1
    while end > 0:
        comparison += 1
        mass[end], mass[0] = mass[0], mass[end]
        exchange += 1
        siftDown(mass, 0, end - 1)
        end -= 1
    return(('зміни'),exchange, ('зрівнення'), comparison, mass)


def shell(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    inc = len(mass) // 2
    while inc:
        for i, el in enumerate(mass):
            while i >= inc and mass[i - inc] > el:
                exchange += 1
                mass[i] = mass[i - inc]
                i -= inc
            mass[i] = el
            comparison += 1
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return (('зміни'), exchange, ('зрівнення'), comparison, mass)



while True:
    try:

        comparison = 0
        exchange = 0
        do = int(input('яким методом відсортувати масив?(1 - сортування перемішуванням, '
                       '2 - пірамідальне сортування, 3 - сортування Шелла)\n (4 - сортування бульбашкою, '
                       '5 - сортування вибором, 6 - сортування перемішуванням)\n'))
        text = input('бажаєте ввести масив вручну(1) чи згенерувати(2) послідовність(100000 елементів)?')
        if text == '1':
            mass = np.array(input('введіть масив(елементи повинні бути через кому): ').split(', '), dtype=int)
        elif text == '2':
            mass = np.array(random.sample(range(100000), 10000), dtype=int)
        else:
            print('введіть правельне значення')
        flag = True
        n = len(mass)
        while flag:
            flag = False
            if do == 1:
                print(cocktailsort(mass, comparison, exchange))
            elif do == 2:
                print(heapsort(mass, comparison, exchange))
            elif do == 3:
                print(shell(mass, comparison, exchange))
            elif do == 4:
                print(bubblesort(mass, comparison, exchange))
            elif do == 5:
                print(insertionsort(mass, comparison, exchange))
            elif do == 6:
                print(selectionsort(mass, comparison, exchange))
            else:
                print('введіть правельне значення')
                flag = True


    except ValueError:
        print("Введіть правельне значення")
    while True:
        doo = input("Бажаєте продовжити ?(y /n )\n")
        if doo == "y" or doo == "n":
            break
        print('Не коректні данні!')
    if doo == "y":
        continue
    if doo == "n":
        break