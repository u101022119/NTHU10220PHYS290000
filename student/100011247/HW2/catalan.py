catalan = range(1,10001)
for i in range(10000):
     catalan[i+1]=(4*i+2)*catalan[i]/(i+2)
     if catalan[i+1] > 1000000000:
       a=i
       break
print catalan[0:i]


