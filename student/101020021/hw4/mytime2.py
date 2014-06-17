class Time:
    def __init__ (self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s
    def to_second(self):
        s = self.hour * 3600
        s += self.minute * 60
        s += self.second * 1
        return s
    def print_time(self):
        a,b,c = self.hour,self.minute,self.second
        print '{0:02d} : {1:02d} : {2:02d}'.format(a,b,c)
    def is_after(t1,t2):
        th = t1.hour > t2.hour
        tm = t1.hour == t2.hour and t1.minute > t2.minute
        ts = t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second
        ans = th or tm or ts
        print ans
        return ans
    def increment_modifier(self,s):
        s = int(s) + self.to_second()
        h = s/3600 
        s = s%3600
        m = s/60 
        s = s%60
        self.hour , self.minute , self.second = h,m,s
        self.print_time()
        return self
    def increment_pure(self,s):
        s = int(s) + self.to_second()
        h = s/3600 
        s = s%3600
        m = s/60 
        s = s%60
        ans = Time(0,0,0)
        ans.hour , ans.minute , ans.second = h,m,s
        self.print_time()
        ans.print_time()
        return ans
    def mul_time(self,a):
        s = self.to_second()
        s *= a
        ans = Time(0,0,0)
        ans.increment_modifier(s)
        return ans
#    def __lt__(self,T2):
#        t1, t2 = self.to_second(), T2.to_second()
#        if t1 < t2:
#            return True
#        else:
#            return False
#    def __gt__(self,T2):
#        t1, t2 = self.to_second(), T2.to_second()
#        if t1 > t2:
#            return True
#        else:
#            return False
#    def __eq__(self,T2):
#        t1, t2 = self.to_second(), T2.to_second()
#        if t1 == t2:
#            return True
#        else:
#            return False
    def __cmp__(self,T2):
        t1, t2 = self.to_second(), T2.to_second()
        if t1 > t2:
            return 1
        elif t1 < t2:
            return -1
        else:
            return 0

T = Time(8,0,0)
T2 = Time(8,1,0)
T3 = Time(8,1,2)
T.print_time()
T2.print_time()
T3.print_time()
print T > T2 , T == T2 , T < T2


