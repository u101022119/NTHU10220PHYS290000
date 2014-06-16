class Time:
    def __init__ (self,x,y,z):
        self.hour = x
        self.minute = y
        self.second = z
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
    def increment_modifier(self,z):
        z = int(z) + self.to_second()
        x = z/3600 
        z = z%3600
        y = z/60 
        z = z%60
        self.hour , self.minute , self.second = x,y,z
        self.print_time()
        return self
    def increment_pure(self,z):
        z = int(z) + self.to_second()
        x = z/3600 
        z = z%3600
        y = z/60 
        z = z%60
        ans = Time(0,0,0)
        ans.hour , ans.minute , ans.second = x,y,z
        self.print_time()
        ans.print_time()
        return ans
    def mul_time(self,a):
        z = self.to_second()
        z *= a
        ans = Time(0,0,0)
        ans.increment_modifier(z)
        return ans
    def fun(self,dist):
        ans = self.mul_time(1.0/dist)
        return ans

T = Time(9,2,7)

T.print_time()

T1 = T.fun(78)

T.print_time()


