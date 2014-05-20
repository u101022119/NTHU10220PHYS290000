import math
L = int(raw_input("the value of L"))
M = 0
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if(i == 0 and j == 0 and k == 0):
                M = M+0
            elif((i+j+k)%2 == 0):
                M = M+1/math.sqrt(i**2+j**2+k**2)
            else:
                M = M-1/math.sqrt(i**2+j**2+k**2)

print M
            
