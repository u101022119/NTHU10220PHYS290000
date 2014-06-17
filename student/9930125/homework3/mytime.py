
class Time():
    """time that has hours,minutes,and seconds"""
    
def print_time (time):
    print '%.2d:%.2d:%.2d' % (time.hour,time.min,time.s)
    
start= Time()
start.hour=4
start.min=35
start.s=53

print_time(start)

t1=Time()
t2=Time()

t1.hour=7
t1.min=41
t1.s=37

t2.hour=6
t2.min=30
t2.s=25

def is_after(t1, t2):
    return (t1.hour, t1.min, t1.s) > (t2.hour, t2.min, t2.s)

print is_after(t1,t2)

t3=Time()

addsec=3661

def increment_modifier(time,addsec):
    t3.hour,addmin=divmod(addsec,3600)
    t3.min,t3.s=divmod(addmin,60)
    time.hour+=t3.hour
    time.min+=t3.min
    time.s+=t3.s
    if time.s>=60:
        time.s-=60
        time.min+=1
        if time.min>=60:
            time.min-=60
            time.hour+=1
    print_time(time)
    
increment_modifier(start,addsec)


def increment_pure(time,addsec):

    time.hour,totallmin=divmod(time.hour*3600+time.min*60+time.s+addsec,3600)
    time.min,time.s=divmod(totallmin,60)
    print_time(time)
    
increment_pure(start,addsec)

distance=3000.0

def mul_time(time,distance):
    ap=distance/(time.hour*3600+time.min*60+time.s)
    print 'The averge pace is',ap,'seconds per mile.'
mul_time(start,distance)
