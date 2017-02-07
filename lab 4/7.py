'''виконав Насадюк Віталій
 написати програму яка визначає відстань між двома точками з кординами  (х1 у1) і (х2 у2) 
'''
    
while True:
    try :
         x2 = float(input("Введіть координату x2:"))
         x1 = float(input("Введіть координату x1:"))
         y1 = float(input("Введіть координату y1:"))
         y2 = float(input("Введіть координату y2:"))
         d = ((x2 - x1)**2 + (y2-y1)**2)**0.5
         print(d)
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
