import math
L = input("Size of lattice = 2L+1, input L: ")
Vijk = 0.
Vtota = 0.
Vtotb = 0.
Vtotc = 0.
for i in range(L):
  for j in range(L):
     for k in range(L):
          if i!=0 and j!=0 and k!=0:
              Vijk = 1/math.sqrt(i**2+j**2+k**2)*((-1)**(i+j+k))
              Vtota = Vtota + Vijk
          elif i==0 and j==0 and k!=0:
              Vijk = 1/math.sqrt(i**2+j**2+k**2)*((-1)**(i+j+k))
              Vtotb = Vtotb + Vijk                     
          elif i==0 and j!=0 and k!=0:
              Vijk = 1/math.sqrt(i**2+j**2+k**2)*((-1)**(i+j+k))
              Vtotc = Vtotc + Vijk          
              
print "Medelung constant =",8*Vtota+6*Vtotb+12*Vtotc
          



