import math



def madelung(L):
    M=0
    for i in range (-L,L+1):
        for j in range (-L,L+1):
            for k in range (-L,L+1):
                if(i==0 and j==0 and k==0):
                    M=M+0
                elif((i+j+k)%2==0):
                    x= 1/math.sqrt(i**2+j**2+k**2)
                    M=M+x
                elif((i+j+k)%2==1):
                    y=-1/math.sqrt(i**2+j**2+k**2)
                    M=M+y
                

    print M

L = int(raw_input('Enter a const that means it with L atoms in all directions.\n'))
madelung(L)
