import random
n = int(input('введіть скільки елементів в списку'))
mass = [0] * n
for i in range(n):
    mass[i] = random.randint(-n, n)
print(mass)
for i in range(1, n):
    j = i - 1
    key = mass[i]
    while j >= 0 and mass[j] > key:
        mass[j + 1] = mass[j]
        j -= 1
        mass[j +1] = key
print(mass)
