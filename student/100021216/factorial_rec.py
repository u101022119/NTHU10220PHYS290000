def factorial_rec(n):
    if n-int(n)!=0:
        return 'None'
    elif n<0:
        return 'None'
    elif n==0:
        return 1
    else:
        return int(n*factorial_rec(n-1))


n=input('Enter a number:')

m=factorial_rec(n)

print m
