import math
n = float(raw_input('ENTER THE VALUE OF THE N: '))
def factorial_rec(n):
    if n < 0:
        return None
    elif n != int (n):
        return None
    else:
        if n == 0:
            return 1
        else:
            s = int(n)
            return s * factorial_rec(n-1)

print 'THE FACTORIAL N IS ', factorial_rec(n),'.'
