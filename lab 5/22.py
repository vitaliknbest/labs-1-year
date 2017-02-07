while True:
    s = input("введіть строку ")
    l = s.split(" ")
    l = s.lstrip()
    print(s)
    try:
        
        if  not s.endswith("."):
            raise ValueError
        if len(l) in range(2,21):
            while len(l) != 0:
                e = l.pop()
                if len(e) not in range(1,9) or e.isupper() or e.isdigit():
                    raise ValueError
            l = s.split(" ")
            last = l.pop()
            last = last.replace(".", "")
            while len(l) != 0:
                e = l.pop()
                if e != last:
                    for i in range(97, 123):
                        c = chr(i)
                        if e.startswith(c):
                            if e.rfind(c) > 0:
                                print(e)
        else:
            print("Послідовність повинна мати від 2 до 20 слів!!!")
    except ValueError:
        print("Слова мають бути не довші 8 букв в нижньому рєстрі і останнє\
         слово повинно закінчуватись крапкою ")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
