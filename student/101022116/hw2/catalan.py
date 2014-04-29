ca = {0:1}
def Catalan (n):
    if n not in ca:
        ca[n]=(4*n-2.)/(n+1.)*Catalan(n-1)
    return ca[n]

for i in range(0,30):
    print i , Catalan(i) , Catalan(i)>10**12
    
    
