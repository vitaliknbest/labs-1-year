b = int(input('введіть перше число'))
a = int(input('введіть друге  число'))
 
while a!=0 and b!=0:
    if a > b:
        a = a % b
    else:
        b = b % a
 
print (a+b)
def nsd (a, b):
    return abs(a) if b == 0 else nsd(b, a % b)
print(nsd(a, b))
