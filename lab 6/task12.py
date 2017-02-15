#Насадюк В, КНИТ16-А
#Значение переменной x, обозначающее некоторую длину в единицах p, заменить величиной этой же длины в метрах
from enum import Enum


class measure(Enum):
    decimetre = 1
    kilometre = 2    
    metre = 3
    millimetre = 4
    centimetre = 5
while True:
    try:
        print("measure:decimetre, kilometre, metre, millimetre, centimetre  ")
        x = float(input('leght:'))
        p = measure[input('measure:')]
        if p == measure(1):
            x /= 10
        elif p == measure(2):
            x *= 1000
        elif p == measure(3):
            x *= 1
        elif p == measure(4):
            x /=1000 
        elif p == measure(5):
            x /= 100
        else:
            print("введіть коректні дані")   
        print( x)    
        while True:
            do = input("Бажаєте продовжити ?(y /n )\n")
            if do == "y" or do == "n":
                break
            print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
    except ValueError:
        print("Введіть правельне значення")

        
