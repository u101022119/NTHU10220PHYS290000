n=float(raw_input('hello moto'))
def fibonacci_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_rec(n-2)+fibonacci_rec(n-1)

print fibonacci_rec(n)
