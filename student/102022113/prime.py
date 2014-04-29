prime=[2]

for i in range(3,10000+1):
    is_i_prime=True
    for j in range (2,len(prime)):
        if j > (i**0.5):
            break
        elif i%j==0:
            is_i_prime=False
    if is_i_prime:
        prime.append(i)

print prime
        
