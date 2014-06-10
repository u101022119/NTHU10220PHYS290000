# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:45:46 2014

@author: user
"""

import random
def random_list(N,a,b):
    c = []
    for i in range(N):
        c.append(random.randint(a,b))
    return c

def selection_sort(c,N):
    print random.sample(c,N)
    
selection_sort()