# Homewrok 2 Exercise: Prime
prime_list = [2]
import math
n = 3
while n <= 10000:
    i = 0
    while i < len(prime_list):
        if n % prime_list[i] == 0:
            break
        i = i + 1
    if i == len(prime_list):
        prime_list.append(n)
    n = n + 1

print prime_list
