import random


def bubblesort(mass):
    for i in range(1, n+1):
        for j in range(n-1, i-1, -1):
            if (mass[j-1] > mass[j]):
                mass[j], mass[j-1] = mass[j-1], mass[j]
    return(mass)

def selectionsort(mass):
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if mass[j] < mass[min]:
                min = j
        mass[i], mass[min] = mass[min], mass[i]
    return(mass)

def insertionsort(mass):
   for i in range(1, n):
    j = i - 1
    key = mass[i]
    while j >= 0 and mass[j] > key:
        mass[j + 1] = mass[j]
        j -= 1
    mass[j +1] = key
    return(mass)

def cocktailsort(mass):
    for k in range(len(mass)-1, 0, -1):
        swapped = False
        for i in range(k, 0, -1):
            if mass[i]<mass[i-1]:
                mass[i], mass[i-1] = mass[i-1], mass[i]
                swapped = True

        for i in range(k):
            if mass[i] > mass[i+1]:
                mass[i], mass[i+1] = mass[i+1], mass[i]
                swapped = True
      
        if not swapped:
            return(mass)
def heapsort(mass):
    def heapify(mass):
        start = (len(mass) - 2) // 2
        while start >= 0:
            siftDown(mass, start, len(mass) - 1)
            start -= 1

    def siftDown(mass, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and mass[child] < mass[child + 1]:
                child += 1
            if child <= end and mass[root] < mass[child]:
                mass[root], mass[child] = mass[child], mass[root]
                root = child
            else:
                return

    heapify(mass)
    end = len(mass) - 1
    while end > 0:
        mass[end], mass[0] = mass[0], mass[end]
        siftDown(mass, 0, end - 1)
        end -= 1
    return(mass)


n = int(input('введіть скільки має бути елементів в масиві'))
mass = [0]*n
for i in range(n):
    mass[i] = random.randint(0,n)
print(heapsort(mass))
