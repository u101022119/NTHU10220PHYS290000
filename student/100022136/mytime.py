import copy

class Time(object):
    """Time to turn in the homework."""
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)
    def increment_modifier(self,sec_i):
        self.second+=sec_i
        self.minute+=int(self.second/60)
        self.second=self.second%60
        self.hour+=int(self.minute/60)
        self.minute=self.minute%60
    def increment_pure(self,sec_i):
        t=copy.copy(self)
        t.second+=sec_i
        t.minute+=int(t.second/60)
        t.second=t.second%60
        t.hour+=int(t.minute/60)
        t.minute=t.minute%60
        return t
    def mul_time(self,n):
        t1_total=self.hour*3600+self.minute*60+self.second
        t1_total*=n
        self.hour=int(t1_total/3600)
        self.minute=int(t1_total/60)%60
        self.second=t1_total%60
def pace(t,dis):
    t.mul_time(1/dis)
    return 1/t

t1=Time()
t1.hour=1
t1.minute=5
t1.second=45
t1.print_time()

def is_after(t1,t2):
    t1_total=t1.hour*3600+t1.minute*60+t1.second
    t2_total=t2.hour*3600+t2.minute*60+t2.second
    return t1_total>t2_total

t2=Time()
t2.hour=1
t2.minute=6
t2.second=45
t2.print_time()
print is_after(t1,t2)
t2.increment_modifier(3600)
t2.print_time()
t3=t2.increment_pure(3600)
t3.print_time()
t1.mul_time(3)
t1.print_time()

