
cn=1
n=0
Cn=[cn]
while cn<=1000000000:
    cn=cn*(4*n+2)/(n+2)
    n+=1
    Cn.append(cn)

print Cn
