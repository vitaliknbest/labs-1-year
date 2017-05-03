import random
n = int(input('введіть скільки елементів в списку'))
mass = [0] * n
for i in range(n):
    mass[i] = random.randint(-n, n)
print(mass)
for i in range(n - 1):
    min = i
    for j in range(i + 1, n):
        if mass[j] < mass[min]:
            min = j
        mass[i], mass[min] = mass[min], mass[i]
print(mass)


