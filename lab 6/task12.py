from enum import Enum


class measure(Enum):
    decimetre = 1
    kilometre = 2    
    metre = 3
    millimetre = 4
    centimetre = 5
    x = float(input('leght:'))
    p = [input('measure:')]
    if p == measure.decimetre:
        x *= 0.1
    elif p == 2:
        x *= 1000
    elif p == 3:
        x *= 1
    elif p == 4:
        x *= 0.001
    elif p == 5:
        x *= 0.01
    else:
        print("введіть коректні дані")

    
    
