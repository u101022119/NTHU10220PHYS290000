import math

prime=[2]

i=3
while i<10000:
    n=0
    while True:
        if math.sqrt(i)<prime[n]:
            prime.append(i)
            break
        else:
            if i%prime[n]==0:
                break
        n+=1
    i+=1

print prime
