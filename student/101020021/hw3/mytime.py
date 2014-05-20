# -*- coding: utf-8 -*-
"""
Created on Tue May 13 15:58:32 2014

@author: user
"""

class Time(object):
    ''''''
    
def print_time(t):
    print '(%.2d : %.2d : %.2d)' %  (t.hour,t.minute,t.second)
    
def is_after(t1,t2):
    greater_smaller_equal((t1.hour-t2.hour)*3600+(t1.minute-t2.minute)*60+(t1.second-t2.second),0)
        
def greater_smaller_equal(a,b):
    while a<b:
        print True
        break
    while a>=b:      
        print False
        break

def increment_modifier(t,num):
    sum=t.hour*3600+t.minute*60+t.second+num
    a=sum//3600
    b=(sum-a*3600)//60
    c=sum % 60
    t.hour=a
    t.minute=b
    t.second=c

def increment_pure(t,num):
    sum=t.hour*3600+t.minute*60+t.second+num
    new_time=Time()
    new_time.hour=sum//3600
    new_time.minute=(sum-new_time.hour*3600)//60
    new_time.second=sum % 60
    return new_time

def mul_time(t,num):
    sum=(t.hour*3600+t.minute*60+t.second)*num
    new_time=Time()
    new_time.hour=sum//3600
    new_time.minute=(sum-new_time.hour*3600)//60
    new_time.second=sum % 60
    return new_time

def average_pace(t,distance):
    return mul_time(t,1.0/distance)

t=Time()
t.hour=12
t.minute=55
t.second=43

t1=Time()
t2=Time()
t1.hour=1
t1.minute=16
t1.second=22
t2.hour=16
t2.minute=7
t2.second=18

print_time(t)

is_after(t1,t2)

new_time_1=increment_pure(t,1000)
print_time(new_time_1)
print_time(t)

increment_modifier(t,1000)
print_time(t)

new_time_2=mul_time(t,1000)
print_time(new_time_2)
print_time(t)

new_time_3=average_pace(t,1357)
print_time(new_time_3)