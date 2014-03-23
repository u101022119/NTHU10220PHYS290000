def fibonacci_rec(n):
     if float(n) != int(n):
         print 'fibonacci is only defined for integers.'
         return None
     elif n<0:
         print 'fibonacci is not defined for negative integers.'
         return None
     elif n == 0:
         return 0
     elif n ==1 :
         return 1
     else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
