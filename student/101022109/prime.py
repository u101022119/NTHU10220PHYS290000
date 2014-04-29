n=10000
prime=[]
for k in range(2,n+1):
    k_prime=True
    for i in range(len(prime)):
        if prime[i]>int(k**0.5):
            break
        if k%prime[i]==0:
            k_prime=False
            break
    if k_prime:
        prime.append(k)
print prime
