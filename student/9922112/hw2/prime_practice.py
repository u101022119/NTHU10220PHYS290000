# -*- coding: utf-8 -*-
"""
Created on Mon May 12 23:25:01 2014

@author: Administrator
"""
L=[]
def judge_prime(y):
    x=int(math.sqrt(y))
    while x>1:
        if y%x==0:
            break
        x-=1
    else:
        L.append(y)
def prime(n):
    if n<=1 or type(n)!=int:
       print"n must be an integer>1!"
    else: 
        while n>1:
            judge_prime(n)
            n=n-1
        print L   
prime(100000)

    
    





        



    



    
