import random
n = int(input('введіть скільки має бути елементів в масиві'))
mass = [0]*n
for i in range(n):
    mass[i] = random.randint(0,n)
print(mass)
for i in range(1, n+1):
    for j in range(n-1, i-1, -1):
        if (mass[j-1] < mass[j]):
            mass[j], mass[j-1] = mass[j-1], mass[j]
print(mass)
