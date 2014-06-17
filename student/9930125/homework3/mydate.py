class Date(object):
    def print_date(self):
        print '%d/%.2d/%.2d' % (self.year,self.month,self.day)
        
    def increment_date(self,date):
        self.day += date
        while True:
            if self.year%4 == 0 and self.month == 2 :
                if self.day > 29:
                    self.day -= 29
                    self.month += 1
                else:
                    break
            elif self.month <8:
                if self.month % 2 == 1:
                    if self.day > 31:
                        self.day -= 31
                        self.month += 1
                    else:
                        break
                elif self.month == 2:
                    if self.day > 28:
                        self.day -=28
                        self.month += 1
                    else:
                        break
                else:
                    if self.day > 30:
                        self.day -= 30
                        self.month += 1
                    else:
                        break
            else:
                if self.month == 12:
                    if self.day > 31:
                        self.day -= 31
                        self.month = 1
                        self.year += 1
                    else:
                        break
                elif self.month % 2 == 0:
                    if self.day > 31:
                        self.day -= 31
                        self.month += 1
                    else:
                        break
                else:
                    if self.day >30:
                        self.day -= 30
                        self.month += 1
                    else:
                        break

        Date.print_date(self)

date = Date()
date.year = float(raw_input('year: '))
date.month = float(raw_input('month: '))
date.day = float(raw_input('day: '))

Date.increment_date(date,float(raw_input('increment: ')))
                    
