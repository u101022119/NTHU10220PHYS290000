n = float( raw_input('Enter the value of n:'))
def fibonacci_rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n==int(n) and n>= 3:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
print fibonacci_rec(n)
