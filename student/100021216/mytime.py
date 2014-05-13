import copy

class time(object):
    """Represents time"""
    
time1=time()
time1.hour=10
time1.minute=14
time1.second=6

time2=time()
time2.hour=4
time2.minute=16
time2.second=6

def print_time(time):
    print '%.2d:%.2d:%.2d' % ( time.hour, time.minute, time.second)

def time_to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second

def is_afer(time1,time2):
    if time_to_second(time1) > time_to_second(time2):
        return True
    else:
        return False

def increment_modifier(time,seconds):
    time.second += seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def increment_pure(time,seconds):
    global newtime
    newtime=copy.deepcopy(time)
    newtime.second += seconds
    while newtime.second >= 60:
        newtime.second -= 60
        newtime.minute += 1
    while newtime.minute >= 60:
        newtime.minute -= 60
        newtime.hour += 1

def mul_time(time,N):
    second=time_to_second(time)*N
    hour=0
    minute=0    
    while second>3600:
        second-=3600    
        hour+=1 
    while second>60:
        second-=60
        minute+=1   
    global newtime
    newtime=copy.deepcopy(time)
    newtime.hour = hour
    newtime.minute = minute
    newtime.second = second
    return newtime
    
def average_pace(time,distance):
    return mul_time(time,1.0/distance)
