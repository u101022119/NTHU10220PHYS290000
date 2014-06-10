import copy
import math

class Time(object):
    """Represents time"""

time1 = Time()
time1.hour = 6
time1.minute = 30
time1.second = 6

def print_time(time):
    print '%.2d:%.2d:%.2d' % ( time.hour, time.minute, time.second)    
    
def time_to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second
    
def mul_time( time, number):
    
    second = time_to_second(time) * number
    hour = 0
    minute = 0    
    
    while second - 3600 > 0 :
        second -= 3600    
        hour += 1 
         
    while second - 60 > 0 :
        second -= 60
        minute += 1
    
    newtime = Time()
    newtime.hour = hour
    newtime.minute = minute
    newtime.second = second
    
    return newtime
    
def average( time, distance):
    # 1.0 , float
    return mul_time( time, 1.0/distance)
    

