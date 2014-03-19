import math

def fibonacci_rec(n):
    
    if n<0 :
        return None
    elif n==1 or n==0 :
        return 1
    elif n%1.0==0:
       temp = fibonacci_rec(n-2) + fibonacci_rec(n-1)
       return temp 

n = float(raw_input())

i = 0

while i < n:
    print fibonacci_rec(i)
    i+=1

