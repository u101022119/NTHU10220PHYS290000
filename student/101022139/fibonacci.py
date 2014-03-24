import math
n = float(raw_input('ENTER THE VALUE OF THE N: '))
def fibonacci_rec(n):
    if n < 0:
        return None
    elif n != int (n):
        return None
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci_rec(n-1) +fibonacci_rec(n-2)


def print_fib(n):
    f1, f2 =  1,  1
    while f1 <=  fibonacci_rec(n):
        print(f1)
        f1, f2 =  f2, f1+f2


print print_fib(n)
