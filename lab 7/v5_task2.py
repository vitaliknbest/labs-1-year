# Насадюк Віталій
#Дана непустая последовательность слов из строчных руссских букв; между соседними словами -
# - запятая, за последним словом - точка. Вывести на экран в алфавитном порядке все звонкие
# согласные буквы, которые входят только в одно слово.
def isIntersection(word1,word2):
    return len(word1 & word2) !=0

def intersection(word1,word2):
    return word1 & word2


while True:
    try:
        buk = set('бвгджзйклмнпрстфхцчшщ')
        s = input('Ведіть слова ( через кому ) а в кінці крапку\n')
        spusok = set()
        listt = []
        if s.endswith('.'):
            s = s.split(',')
            n = len(s)
            for i in s:
                listt.append(intersection(buk, set(i)))
            hasIntersction = [False] * n
            for i in range(len(listt) - 1):
                for  j in range(i + 1, len(listt)):
                    if intersection(listt[i], listt[j]):
                        hasIntersction[i]=True
                        hasIntersction[j]=True
            for i in range(len(listt)):
                if(not(hasIntersction[i])):
                    print(sorted(listt[i]))
        else :
            raise ValueError
        
    except ValueError:
        print("Ведіть слова російськими буквами через кому а за останнім крапку\n")
    while True:
        do = input("Бажаєте продовжити ?(y /n )\n")
        if do == "y" or do == "n":
            break
        else :
            print('Не коректні данні!')
    if do == "y":
        continue
    if do == "n":
        break
