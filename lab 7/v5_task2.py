# Насадюк Віталій
#Дана непустая последовательность слов из строчных руссских букв; между соседними словами -
# - запятая, за последним словом - точка. Вывести на экран в алфавитном порядке все звонкие
# согласные буквы, которые входят только в одно слово.

while True:
    try:
        buk = set('бвгджзйклмнпрстфхцчшщ')
        s = input('Ведіть слова ( через кому ) а в кінці крапку\n')
        spusok = set()
        if s.endswith('.'):
            s = s.split(',')
            for i in buk:
                for j in s:
                 if j.count(i) != 0 and str(list(s)-list(j)).count(i)==0 :
                     spusok.add(i)
            print(sorted(spusok))
        else :
            raise ValueError
        
    except ValueError:
        print("Ведіть слова російськими буквами через кому а за останнім крапку\n")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        print('Не коректні данні!')
        if do == "y":
            continue
        if do == "n":
            break
