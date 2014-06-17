import math
prime=[2]
n=3

while n<=10000:
    i = 1
    while i<=math.sqrt(n):
        if n%(i+1)==0:
            i=i+1
            break
        elif  i == int(math.sqrt(n)):
            prime.append(n)
        i=i+1
    n = n+1
        
print prime
