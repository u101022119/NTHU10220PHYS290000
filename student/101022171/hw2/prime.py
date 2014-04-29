"""
#File:   prime.py
#Title:  Prime
#Due:    4/29/2014
#Author: 101022171, chin-hua Cheng
"""


def prime(n):
    d = 2
    while d**2<=n:
        if (n%d==0):
            return False
        d+=1
    return True

count = 0
i = 2
while True:   
    if prime(i):
        if count == 1000:
            break
        print i
        count +=1
        i +=1
        continue
    i +=1
