def factorial_rec(n):    
    if n == 0:
        return 1
    else:
        rec = factorial_rec(n-1)
        result = n*rec
        return result
    
a = int(raw_input('Put an integer:'))
if a < 0:
    print 'None'
else:
    print factorial_rec(a)

            
        
