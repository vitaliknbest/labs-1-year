#Насадюк Віталій КНІТ 16-а
# написати програму  створення на системному диску в каталозі NewFold свого каталого, в ньому текстого файлу з анкетою і
# вфомрувати код програмного виводу на екран анкети
import os
flag = True
while True:
    os.chdir('D:/NewFold/')
    os.chdir('D:/NewFold/Fold')
    print('анкета :)')
    while flag:
        name = input('Ведіть своє імя\n')
        if not (name.isalpha() and name.istitle()):
            print('некоректне значення')
        else:flag = False
    flag = True
    while flag:
        year = input('скільки вам років?\n')
        if not  year.isdigit() and int(year)  in range(5,110):
            print('неможливе значення')
        else:flag = False
    flag = True
    while flag:
        numb = input('введіть свій номер \n')
        if numb.isalpha() and len(numb) != 12:
            print('невірний номер')
        else:flag = False
    flag = True
    while flag:
        email = input('введіть свою електронну пошту\n')
        if '@' and '.' not  in email:
            print('некоректний емейл')
        else: flag = False
    with open('Anket.txt', 'w') as g:
        g.write('Імя: ' + name + '\n')
        g.write('Вік: ' + year + '\n')
        g.write('Моб. номер: ' + numb + '\n')
        g.write('Электронна адреса: ' + email + '\n')
    with open('Anket.txt', 'r') as f:
        f = f.read()
    print(f)
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break