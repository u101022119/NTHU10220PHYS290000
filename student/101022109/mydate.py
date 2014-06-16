class Date :
    def __init__(self,x,y,z):
        self.day = int(x)
        self.month = int(y)
        self.year = int(z)
    def print_date(self):
        print '{0} / {1} / {2}'.format(self.month,self.day,self.year)
    def increment_date(self,n = 0):
        x,y,z = self.day , self.month , self.year
        x += n
        ans = Date(x,y,z)
        change = True
        while change == True:
            ans.print_date()
            change = False
            if y in {1,3,5,7,8,10,12}:
                if x >= 31:
                    x,y = x - 31, y + 1
                    change = True
            elif y in {4,6,9,11}:
                if x >= 30:
                    x,y = x- 30, y + 1
                    change = True
            elif y ==2:
                if z%4 != 0:
                    leapyear = False
                elif z%100 != 0:
                    leapyear = True
                elif z%400 != 0:
                    leapyear = False
                else:
                    leapyear = True
                if leapyear == True:
                    if x >= 29:
                        x,y = x - 29, y + 1
                        change = True
                elif leapyear == False:
                    if x >= 28:
                        x,y = x - 28,y + 1
                        change = True
            if y > 12:
                y,z = y - 12, z + 1
                change = True
            ans = Date(x,y,z)
        return ans
        print 'finish!'

D = Date(6,16,2014)

D.increment_date(500)

