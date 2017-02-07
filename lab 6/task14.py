from enum import Enum


class Year(Enum):
    grean = 0
    red = 1
    yellow = 2
    wite = 3
    black = 4

class Animals(Enum):

    rat = 0
    cow = 1
    tiger = 2
    rabbit = 3
    dragon = 4
    snake = 5
    horse = 6
    sheep = 7
    monkey = 8
    chicken = 9
    dog = 10
    pig = 11
date = int(input('Введіть будь-ласка  рік'))
date -= 4
date %= 60
counter = 0
while date >= 12:
    date -=12
    counter += 1
print(Year(counter).name,Animals(date).name)
