# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 15:37:34 2014

@author: Administrator
"""

import random

def random_list(N,a,b):
    R = []
    for i in range(N):
        R.append(random.randint(a,b))
    return R

