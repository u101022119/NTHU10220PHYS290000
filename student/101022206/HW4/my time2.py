# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 16:02:32 2014

@author: user
"""

class Time(object):
    def __cmp__(self,other):
        if self.hour > other.hour:
            print 'Time1 is ahead Time2'
            return 1 
        elif self.hour < other.hour:
            print 'Time2 is ahead Time1'
            return -1
        else:
            if self.minute > other.minute:
                print 'Time1 is ahead Time2'
                return 1
            elif self.minute < other.minute:
                print 'Time2 is ahead Time1'
                return -1
            else:
                if self.second > other.second:
                    print 'Time1 is ahead Time2'
                    return 1
                elif self.second < other.second:
                    print 'Time2 is ahead Time1'
                    return -1
                else:
                    print 'Time1 = Time2'
                    return 0

Time1 = Time()
Time2 = Time()

Time1.hour = 2
Time1.minute = 20
Time1.second = 23
Time2.hour = 2
Time2.minute = 20
Time2.second = 23

cmp(Time1,Time2)