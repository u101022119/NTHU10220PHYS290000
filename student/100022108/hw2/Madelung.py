def madelung_constant(L):
    V_sum = 0
    for i in range (-L,L):
        for j in range (-L,L):
            for k in range (-L,L):
                if i == j == k == 0:
                    V_temp = 0
                else:
                    V_temp =(-1)**(i+j+k)/((i**2+j**2+k**2)**(0.5))  
                    V_sum = V_sum + V_temp
                    
    print V_sum
            
print 'correct madelung_constant=-1.748'

M = int(raw_input("Enter L of madelung constant: "))
print M
madelung_constant(M)


