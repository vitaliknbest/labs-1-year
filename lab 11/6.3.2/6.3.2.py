#Насадюк Віталій КНІТ 16-а
#  дані текстові файли f і g, хаписати в файл h  спочатку компоненти файла f, а потім компоненти файла g

g = open('g.txt', 'w')
f = open('f.txt', 'w')
f.write(input('введіть текст для f: '))
g.write(input('введіть тескт для g: '))
f.close()
g.close()
g = open('g.txt', 'r').read()
f = open('f.txt', 'r').read()
h = open('h.txt', 'a')
h.write(f)
h.write('\n')
h.write(g)
h.close()
