def fibonacci_rec(n):
    if n-int(n)!=0:
        return 'None'
    elif n<0:
        return 'None'
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return int(fibonacci_rec(n-1)+fibonacci_rec(n-2))
        
        
def fibonacci(n):
    m=0
    while m<=n:
        print fibonacci_rec(m)
        m+=1



