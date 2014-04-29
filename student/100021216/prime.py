from __future__ import division

p=[2]
n=3
while n<=10000:
    a=0
    b=0
    for x in p:
        if x<n**0.5:
            b+=1
            if n//x-n/x==0:
                break
            else:
                a+=1
        else:
            break
    if a==b:
        p.append(n)
    n+=1
    
print p    
