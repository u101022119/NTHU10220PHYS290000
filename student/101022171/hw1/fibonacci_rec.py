#File: fibonacci_rec.py
#HW1_EX9_Fibonacci_function
#Due: 3/25/2014
#Author: 101022171

def fibonacci_rec (n):
    if not isinstance(n, int):
        print "Fibonacci series are only defined for integers!"
        return None
    elif n < 0:
        print "Fibonacci series are not defined for negative integers!"
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  fibonacci_rec (n - 1) + fibonacci_rec (n - 2)

#demo here
print fibonacci_rec(7)
fibonacci_rec(1.5)
fibonacci_rec(-1)
fibonacci_rec(-2.5)
