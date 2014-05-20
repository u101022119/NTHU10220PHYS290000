def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

a = float(raw_input('Put an integer:'))

m = 0
if a <0:
    print 'None'
else:
    while m < a:
        print fibonacci_rec(m),' ',
        m = m + 1
        
    
