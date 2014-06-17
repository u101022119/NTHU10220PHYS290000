class Time:
    def __init__ (timing,h,m,s):
        timing.hour = h
        timing.minute = m
        timing.second = s
    def to_second(timing):
        s = timing.hour * 3600
        s += timing.minute * 60
        s += timing.second * 1
        return s
    def print_time(timing):
        a,b,c = timing.hour,timing.minute,timing.second
        print '{0:02d} : {1:02d} : {2:02d}'.format(a,b,c)
    def is_after(t1,t2):
        th = t1.hour > t2.hour
        tm = t1.hour == t2.hour and t1.minute > t2.minute
        ts = t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second
        ans = th or tm or ts
        print ans
        return ans
    def increment_modifier(timing,s):
        s = int(s) + timing.to_second()
        h = s/3600 
        s = s%3600
        m = s/60 
        s = s%60
        timing.hour , timing.minute , timing.second = h,m,s
        timing.print_time()
        return timing
    def increment_pure(timing,s):
        s = int(s) + timing.to_second()
        h = s/3600 
        s = s%3600
        m = s/60 
        s = s%60
        ans = Time(0,0,0)
        ans.hour , ans.minute , ans.second = h,m,s
        timing.print_time()
        ans.print_time()
        return ans
    def mul_time(timing,a):
        s = timing.to_second()
        s *= a
        ans = Time(0,0,0)
        ans.increment_modifier(s)
        return ans
    def __cmp__(timing,T2):
        t1, t2 = timing.to_second(), T2.to_second()
        if t1 > t2:
            return 1
        elif t1 < t2:
            return -1
        else:
            return 0

T = Time(8,0,0)
T2 = Time(8,5,0)
T3 = Time(8,5,2)
T.print_time()
T2.print_time()
T3.print_time()
print T > T2 , T == T2 , T < T2


