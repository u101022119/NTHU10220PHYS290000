i=0
a=[1]
while(a[i]<=1000000):
    a.append(a[i]*(4*i+2)/(i+2))
    i+=1
print a