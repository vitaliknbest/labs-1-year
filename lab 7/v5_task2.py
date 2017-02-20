k = set('бвгджзйклмнпрстфхцчшщ')
s = input('Ведіть слова ( через кому ) а в кінці крапку')
sett = set()
for i in s:
    if s.count(i) == 1 and k & set(i) != set() :
        sett.add(i)
print(sorted(sett))
