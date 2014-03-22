#Homework 1 exercise 9
def fibonacci_rec(n):
    if type(n) != int or n < 0:
        return 'None'
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def print_fibonacci_rec(n):
    m = 0
    while m < n:
        print fibonacci_rec(m)
        m = m + 1
        if m == n:
            break
    return fibonacci_rec(n)

