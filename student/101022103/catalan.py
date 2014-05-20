def catalan(n):
    if n == 0:
        return 1
    else:
        return int((4*n-2.0)/(n+1)*catalan(n-1))
                
q= int(raw_input('input integer:'))
for i in range(q+1):
    print catalan(i)
