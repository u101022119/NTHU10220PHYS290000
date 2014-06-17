def catalan(n):
    if n == 0:
        return 1
    else:
        return int((4*n-2.0)/(n+1.0)*catalan(n-1))
                
x = int(raw_input('Enter an integer:'))
for i in range(x+1):
    print catalan(i)
