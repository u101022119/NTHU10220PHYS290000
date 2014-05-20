# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:17:36 2014

@author: user
"""

class Time():
    """time that
    have hours,minutes,and seconds"""
    
def print_time (time):
    print '%.2d:%.2d:%.2d' % (time.hour,time.min,time.s)
    
start= Time()
start.hour=3
start.min=40
start.s=59

print_time(start)

t1=Time()
t2=Time()

t1.hour=9
t1.min=45
t1.s=40

t2.hour=6
t2.min=30
t2.s=25

def is_after(t1,t2):
    first=t1.hour*3600+t1.min*60+t1.s
    second=t2.hour*3600+t2.min*60+t2.s
    if first>second:
        print True
    else :
        print False
is_after(t1,t2)

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
    print 'the averge pace is',ap,'s/mile'
mul_time(start,distance)

