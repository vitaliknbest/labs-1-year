from enum import Enum


class country(Enum):
    Germany = 1
    Cuba = 2
    Laos = 3
    Manoco = 4
    Bangladesh = 5
    Ukraine = 6

    
class continente(Enum):
    Asia = 1
    America = 2
    Europe = 3

s = country[input("country: ")]
while True:
    if s == country(2):
            print(continente(2))
            break
    elif s == country(3) or s == country(5):
            print(continente(1))
            break
    elif s == country(1) or s == country(6) or s == country(4):
            print(continente(3))
            break
    else:
        print('некоректні дані')


