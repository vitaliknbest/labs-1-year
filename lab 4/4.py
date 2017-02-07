'''
виконав Насадюк Віталій
написати програму яка визначає хначення кута в градусах між положенням часової стрілки  на початку доби і її полодженням в hours годин '''
a = 30.0
b = 0.5
c = 0.008333333333333
d = 360
while True:
    while True:
        try:
            while True:

                time = input("Введіть час будь-ласка у 24- x годинному форматі (зразок : 11:56:01) :\n")
                t = time.split(':')
                if len(t)!= 3:
                    raise ValueError
                    
                hours = int(t[0])
                minutes = int(t[1])
                seconds = int(t[2])
                if hours not in range(0, 24) or minutes not in range(0, 60) or seconds not in range(0, 60):
                    print("Введіть правельний час")
                    continue
                else:
                    corner = a * hours + b * minutes + c * seconds
                    if hours not in range (0,12):
                        corner = corner - d
                    print('corner = ', corner)
                break
            break
        except ValueError:
             print("Введіть правельне значення")
    while True:
         do = input("Бажаєте продовжити ?(y /n )\n")
         if do == "y" or do == "n":
             break
         print('Не коректні данні!')
    if do == "y":
         continue
    if do == "n":
         break
