#Насадюк В, КНИТ16-А
#Значение переменной x, обозначающее некоторую длину в единицах p, заменить величиной этой же длины в метрах
from enum import Enum


class measure(Enum):
    decimetre = 1
    kilometre = 2    
    metre = 3
    millimetre = 4
    centimetre = 5
    x = float(input('leght:'))
    p = [input('measure:')]
    if p == measure(1):
        x *= 0.1
    elif p == measure(2):
        x *= 1000
    elif p == measure(3):
        x *= 1
    elif p == measure(4):
        x *= 0.001
    elif p == measure(5):
        x *= 0.01
    else:
        print("введіть коректні дані")
print(x)
    
    
