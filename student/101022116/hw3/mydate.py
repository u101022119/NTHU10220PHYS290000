class Date :
    def __init__(self,mm,dd,yy):
        self.day = int(dd)
        self.month = int(mm)
        self.year = int(yy)
    def print_date(self):
        print '{0} / {1} / {2}'.format(self.month,self.day,self.year)
    def increment_date(self,n = 0):
        dd , mm , yy = self.day , self.month , self.year
        dd += n
        ans = Date(mm,dd,yy)
        change = True
        while change == True:
            ans.print_date()
            change = False
            if mm in {1,3,5,7,8,10,12}:
                if dd >= 31:
                    dd,mm = dd - 31, mm + 1
                    change = True
            elif mm in {4,6,9,11}:
                if dd >= 30:
                    dd,mm = dd - 30, mm + 1
                    change = True
            elif mm ==2:
                if yy%4 != 0:
                    leapyear = False
                elif yy%100 != 0:
                    leapyear = True
                elif yy%400 != 0:
                    leapyear = False
                else:
                    leapyear = True
                if leapyear == True:
                    if dd >= 29:
                        dd,mm = dd - 29, mm + 1
                        change = True
                elif leapyear == False:
                    if dd >= 28:
                        dd,mm = dd - 28,mm + 1
                        change = True
            if mm > 12:
                mm,yy = mm - 12, yy + 1
                change = True
            ans = Date(mm,dd,yy)
        print 'It is done !!'
        return ans 

D = Date(5,14,2014)
##D.print_date()
D.increment_date(400)
