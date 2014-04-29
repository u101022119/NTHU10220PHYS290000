#File: factorial_rec.py
#HW1_EX8_Factorial_function
#Due: 3/25/2014
#Author: 101022171


def factorial_rec (n):
    if not isinstance(n, int):
        print "Factorial is only defined for integers!"
        return None
    elif n < 0:
        print "Factorial is not defined for negative integers!"
        return None
    elif n == 0:
        return 1
    else:
        return  n * factorial_rec (n - 1)


print factorial_rec(5)
factorial_rec(1.5)
factorial_rec(-1)
factorial_rec(-2.5)
