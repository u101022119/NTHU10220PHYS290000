n=raw_input('n= ')

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def p_fib(n):
    for x in range(1,int(n)+1):
        print fib(x)

def is_int(n):
    for x in n:
        if x<'0' or x>'9':
            return False
    return True

def fibonacci_rec(n):
    if is_int(n):
        k=int(n)
        return p_fib(k)
    else:
        print 'error'
        return None

fibonacci_rec(n)
