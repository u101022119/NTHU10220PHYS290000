def fibonacci_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>0 and n==int(n):
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)
    else:
        return 'None!!!'

def give_fibonacci(n):
    k=n
    n=0
    while n<=k:
        print fibonacci_rec(n)
        n=n+1
