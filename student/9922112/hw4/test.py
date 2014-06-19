# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 09:18:37 2014

@author: Administrator
"""
def kind(n,ranks):
    for r in ranks:
        if ranks.count(r)==n: 
            return r
        else:
            pass
    return L

def has_two_pairs(ranks):
    n=0
    for r in ranks:
        if ranks.count(r)>=2:
            n=n+1
    return n/2>=2
    
def has_three_of_a_kind(ranks):
    n=0
    for r in ranks:
        if ranks.count(r)>=3:
            n=n+1
    return n/2>=2
def kind(n,ranks):
    for r in ranks:
        if ranks.count(r) >=n:
            return 'True'
        else:
            pass
            
        
           

def two_pair(ranks):
    pair = kind(2,ranks)
    lowpair = kind(2,list(reversed(ranks)))
    print (pair and lowpair)
    if pair and lowpair !=pair:
        return (pair,lowpair)
    else:
        return None
  

H=[]
h=Hand
