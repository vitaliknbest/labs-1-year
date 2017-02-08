class Date:
    days = range(1, 32)
    month = range(1, 13)
    years = range(1901, 2020)
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def idate(self):
        self.iday()

    def iday(self):
        self.d += 1
        if self.d not in self.days:
            self.d = 1
            self.imonth()

    def imonth(self):
        self.m += 1
        if self.m not in self.month:
            self.m = 1
            self.iyear()

    def iyear(self):
        self.y += 1
        if self.y not in self.years:
            self.years[self.y]


d,m,y = int(input('day :')), int(input('month :')), int(input('year :'))
if d in range(1,32) and m in range(1,13) and y in range(1901,2020):
    date = Date(d, m, y)
    try:
        date.idate()
        print(date.d, '.', date.m, '.', date.y)
    except ValueError:
        print('Invalide date!')
else:
    print('введіть коректні дані')
while True:
    do = input('Бажаэте продовжити?(y / n)')
    while True:
        if do == 'y' or do == 'n':
            break
        else:
            print('введіть будь-ласка y або n')
    if do == 'y':
        continue
    else:
        break
        
