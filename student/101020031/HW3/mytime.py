class Time(object):
    """pass"""
    
def print_time(t):
    print"%.2d:%.2d:%.2d" % (t.hour,t.minute,t.second)    

a=Time()
a.hour=1
a.minute=2
a.second=3

b=Time()
b.hour=2
b.minute=2
b.second=3

print_time(a)

def bigsmall(t1,t2):
    a=t1.hour *3600 + t1.minute*60 + t1.second
    b=t2.hour *3600 + t2.minute*60 + t2.second
    if a<b:
        print "true"
    
    else:
        print "false"
            
def is_after(x,y):
    bigsmall(x,y)
    
def increment_modifier(t1,increase):
    t1.second = t1.second + increase
    if t1.second >= 60:
        t1.second-=60
        t1.minute+=1
    
    if t1.minute >= 60:
        t1.minute-=60
        t1.hour+=1
    






def increment_pure(t1,increase):
    sum = Time()
    sum.second =t1.hour*3600 + t1.minute*60 + t1.second + increase
    if sum.second >= 60:
        sum.second-=60
        sum.minute+=1
    
    if sum.minute >= 60:
        sum.minute-=60
        sum.hour+=1
        
    return sum
    
    
    
    
def mul_time(t1,mul):
    new = Time()
    new.second = t1.second   * mul
    new.minute = t1.minute   * mul
    new.hour   = t1.hour     * mul
    
    if new.second >= 60:
        new.second-=60
        new.minute+=1
    
    if new.minute >= 60:
        new.minute-=60
        new.hour+=1
        
    return new

def average_pace(t,d):
    return  mul_time(t,1.0/d)
