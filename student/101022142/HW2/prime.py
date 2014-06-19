#1-3.prime.py
prime=[2]
for p in range(3,10001):
    i=1
    for n in prime:
        if n<=p**0.5+1:
            if p%n==0:
                i=1
            if p%n!=0:
                i=0
        if i==1:
            break
        if n>p**0.5:
            break
    if i==0:
        prime.append(p)
print prime
