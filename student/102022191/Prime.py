N = 10000

prime= []

for i in range(2,N+1):
    is_i_prime = True
    for j in range(len(prime)):
        if prime[j] > int(i**0.5):
            break
        if i % prime[j] == 0:
            is_i_prime = False
            break
    if is_i_prime:
        prime.append(i)

print prime
