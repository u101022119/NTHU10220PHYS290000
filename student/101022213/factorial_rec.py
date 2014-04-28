def factorial_rec(n):
     if float(n) != int(n):
         print 'Factorial is only defined for integers.'
         return None
     elif n<0:
         print 'Factorial is not defined for negative integers.'
         return None
     elif n == 0:
         return 1
     else:
        return n * factorial_rec(n-1)

