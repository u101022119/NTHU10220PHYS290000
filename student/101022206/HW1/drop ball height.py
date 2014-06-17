# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:54:27 2014

@author: user
"""

def drop_ball_height():
    h1=float(raw_input("Put the height of the tower: "))
    t=float(raw_input("Put the time interval: "))
    h2=h1-0.5*9.8*t*t
    return h2

print drop_ball_height()