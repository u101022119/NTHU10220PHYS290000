def factorial_rec(n):
    if n==0 or n==1:
        return 1
    elif n<0 :
        return None
    elif n%1.0==0 :
        return n*factorial_rec(n-1)
n = float(raw_input())

print factorial_rec(n)
