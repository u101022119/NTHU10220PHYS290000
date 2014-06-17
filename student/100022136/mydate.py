class Date(object):
    def increment_date(self,n):
        cy=[31,28,31,30,31,30,31,31,30,31,30,31]
        ly=[31,29,31,30,31,30,31,31,30,31,30,31]
        d=self.day+n
        while(d>0):
            if self.year%4!=0:
                l=0
            elif self.year%100!=0:
                l=1
            elif self.year%400!=0:
                l=0
            else:
                l=1
            if l==0:
                for i in cy[self.month-1:]:
                    d-=i
                    if d<=0:
                        self.day=d+i
                        break
                    self.month+=1
            if l==1:
                for i in ly[self.month-1:]:
                    d-=i
                    if d<=0:
                        self.day=d+i
                        break
                    self.month+=1
            if d<=0:
                    break
            self.year+=1
            self.month-=12
Dday=Date()
Dday.year=1995
Dday.month=8
Dday.day=1
Dday.increment_date(10000)
print '%dyear%dmonth%dday'%(Dday.year,Dday.month,Dday.day)
