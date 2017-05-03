import random
import numpy as np
from time import time

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
            if side == 1:
                comparison += 1
                if (mass[j - 1] < mass[j]):
                    comparison += 1
                    mass[j], mass[j - 1] = mass[j - 1], mass[j]
                    exchange += 1
            elif side == 2:
                comparison += 1
                if (mass[j - 1 ] > mass[j]):
                    comparison += 1
                    mass[j], mass[j - 1] = mass[j - 1], mass[j]
                    exchange += 1
            else:
                raise ValueError
    return exchange, comparison, mass


def insertionsort( mass, comparison = 0, exchange = 0 ):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    for i in range(1, n):
        j = i - 1
        key = mass[i]
        if side == 1:
            comparison += 1
            while j >= 0 and mass[j] < key:
                comparison += 1
                mass[j + 1] = mass[j]
                j -= 1
                mass[j + 1] = key
                exchange += 1
        elif side == 2:
            comparison += 1
            while j >= 0 and mass[j] > key:
                comparison += 1
                mass[j + 1] = mass[j]
                j -= 1
                mass[j + 1] = key
                exchange += 1
        else:
            raise ValueError

    return  exchange, comparison, mass


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
            if side == 1:
                comparison += 1
                if mass[j] > mass[min]:
                    min = j
                    comparison += 1
                mass[i], mass[min] = mass[min], mass[i]
                exchange += 1
            elif side == 2:
                comparison += 1
                if mass[j] < mass[min]:
                    min = j
                    comparison += 1
                mass[i], mass[min] = mass[min], mass[i]
                exchange += 1
            else:
                raise ValueError
    return exchange, comparison, mass


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
            if side == 1:
                if mass[i] > mass[i-1]:
                    comparison += 1
                    mass[i], mass[i-1] = mass[i-1], mass[i]
                    exchange += 1
                    swapped = True

                for i in range(k):
                    comparison += 1
                    if mass[i] < mass[i+1]:
                        comparison += 1
                        mass[i], mass[i+1] = mass[i+1], mass[i]
                        exchange += 1
                        swapped = True
            elif side == 2:
                if mass[i] < mass[i - 1]:
                    comparison += 1
                    mass[i], mass[i - 1] = mass[i - 1], mass[i]
                    exchange += 1
                    swapped = True

                for i in range(k):
                    comparison += 1
                    if mass[i] > mass[i + 1]:
                        comparison += 1
                        mass[i], mass[i + 1] = mass[i + 1], mass[i]
                        exchange += 1
                        swapped = True
            else:
                raise  ValueError
        if not swapped:
            return exchange, comparison, mass



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
        return exchange, comparison, mass


def shell(mass, comparison=0, exchange=0):
    '''сортує масив в порядку не спаддання

        приймає три параметри:
        1 масив
        2 кількість зрівнень
        3 кількість перестановок
        повертає відсортований масив в порядку не спадання,кількість зрівнень і кількість перестановок '''
    inc = len(mass) // 2
    while inc:
        if side == 1:
            for i, el in enumerate(mass):
                while i >= inc and mass[i - inc] < el:
                    exchange += 1
                    mass[i] = mass[i - inc]
                    i -= inc
                mass[i] = el
                comparison += 1
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
        elif side == 2:
            for i, el in enumerate(mass):
                while i >= inc and mass[i - inc] > el:
                    exchange += 1
                    mass[i] = mass[i - inc]
                    i -= inc
                mass[i] = el
                comparison += 1
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
        else:
            raise ValueError
    return exchange, comparison, mass


while True:
    try:

        comparison = 0
        exchange = 0
        do = int(input('яким методом відсортувати масив?(1 - сортування перемішуванням, '
                       '2 - пірамідальне сортування, 3 - сортування Шелла)\n (4 - сортування бульбашкою, '
                       '5 - сортування вибором, 6 - сортування вставками)\n'))
        text = input('бажаєте ввести масив вручну(1) чи згенерувати(2) послідовність(100000 елементів)?\n')
        side = int(input('введіть як сортувати масив(1 -- спадання, 2 -- зростання )\n'))
        if text == '1':
            mass = np.array(input('введіть масив(елементи повинні бути через кому): ').split(','), dtype=int)
        elif text == '2':
            mass = np.array(random.sample(range(100000), 100000), dtype=int)
        else:
            print('введіть правельне значення')
        flag = True
        n = len(mass)
        while flag:
            flag = False
            if do == 1:
                print('=' * 70 + '\nпочатковий масив: \n{}'.format(mass))
                t = time()
                out = cocktailsort(mass)
                t = time() - t
                print('відсортований масив: \n{}\n'
                  'обміни: {} | зрівнення: {} | час: {:.8f} seconds'
                  '\n'.format(out[2], out[0], out[1], t) + '=' * 70)
            elif do == 2:
                print('=' * 70 + '\nпочатковий масив: \n{}'.format(mass))
                t = time()
                out = heapsort(mass)
                t = time() - t
                print('відсортований масив: \n{}\n'
                  'обміни: {} | зрівнення: {} | час: {:.8f} seconds'
                  '\n'.format(out[2], out[0], out[1], t) + '=' * 70)
            elif do == 3:
                print('=' * 70 + '\nпочатковий масив: \n{}'.format(mass))
                t = time()
                out = shell(mass)
                t = time() - t
                print('відсортований масив: \n{}\n'
                  'обміни: {} | зрівнення: {} | час: {:.8f} seconds'
                  '\n'.format(out[2], out[0], out[1], t) + '=' * 70)
            elif do == 4:
                print('=' * 70 + '\nпочатковий масив: \n{}'.format(mass))
                t = time()
                out = bubblesort(mass)
                t = time() - t
                print('відсортований масив: \n{}\n'
                  'обміни: {} | зрівнення: {} | час: {:.8f} seconds'
                  '\n'.format(out[2], out[0], out[1], t) + '=' * 70)
            elif do == 5:
                print('=' * 70 + '\nпочатковий масив: \n{}'.format(mass))
                t = time()
                out = insertionsort(mass)
                t = time() - t
                print('відсортований масив: \n{}\n'
                  'обміни: {} | зрівннення: {} | час: {:.8f} seconds'
                  '\n'.format(out[2], out[0], out[1], t) + '=' * 70)
            elif do == 6:
                print('=' * 70 + '\nпочатковий масив: \n{}'.format(mass))
                t = time()
                out = selectionsort(mass)
                t = time() - t
                print('відсортований масив: \n{}\n'
                  'обміни: {} | зрівнення: {} | час: {:.8f} seconds'
                  '\n'.format(out[2], out[0], out[1
                                                  ], t) + '=' * 70)
                
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
