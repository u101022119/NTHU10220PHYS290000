import math

def prime():
    x=[2]
    n=3
    k= int(raw_input('Enter the range you want to find primes\n'))
    while n<=k:
        m=0
        while m <= math.sqrt(n):
            m+=1
            if n%(m+1)==0:
                break
            elif m == int(math.sqrt(n)):
                x.append(n)
        n+=1
    print 'These are primes in the range you input\n',x

prime()
            

