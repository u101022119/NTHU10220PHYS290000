import copy

class time(object):
    """Represents time"""
    
time1 = time()
time1.hour = 5
time1.minute = 40
time1.second = 6

time2 = time()
time2.hour = 6
time2.minute = 52
time2.second = 3

def print_time(time):
    print '%.2d:%.2d:%.2d' % ( time.hour, time.minute, time.second)

def time_to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second

def is_afer(time1,time2):
    return time_to_second(time1) > time_to_second(time2)


def increment_modifier(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def increment_pure(time, seconds):
    global newtime
    newtime = copy.deepcopy(time)
    newtime.second += seconds
    if newtime.second >= 60:
        newtime.second -= 60
        newtime.minute += 1
    if newtime.minute >= 60:
        newtime.minute -= 60
        newtime.hour += 1
