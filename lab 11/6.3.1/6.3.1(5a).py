f1 = open('f1.txt', 'r').read(5)
f2 = open('f2.txt', 'r').read(5)
f3 = open('f3.txt', 'r').read(5)
f4 = open('f4.txt', 'r').read(5)
f5 = open('f5.txt', 'r').read(5)
h = open('h.txt', 'a')
h.write(f1)
h.write('\n')
h.write(f2)
h.write('\n')
h.write(f3)
h.write('\n')
h.write(f4)
h.write('\n')
h.write(f5)
h.write('\n')
h.close()
h = (open('h.txt', 'r').read()).split('\n')
f1 = open('f1.txt', 'w')
f1.write(h[4])
f2 = open('f2.txt', 'w')
f2.write(h[3])
f3 = open('f3.txt', 'w')
f3.write(h[0])
f4 = open('f4.txt', 'w')
f4.write(h[1])
f5 = open('f5.txt', 'w')
f5.write(h[2])
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
h = open('h.txt', 'w')
h.close()
