def Madelung_constant(L):
    ML = 0.0
    for i in range(1,L+1):#L^3
        for j in range(1,L+1):
            for k in range(1,L+1):
                increment = (i**2 + j**2 + k**2)**(-0.5)
                if (i+j+k) % 2 == 1:
                    increment *= -1.0
                ML += increment
    ML *= 8.0

    tmp = 0.0
    for i in range(1,L+1):#L^1
        if i%2==1:
            tmp += -1.0/i
        else:
            tmp +=1.0/i
    ML += tmp*6.0

    tmp = 0.0
    for i in range(1,L+1):#L^2
        for j in range(1,L+1):
            if (i+j)%2 ==1:
                tmp -= (i**2 + j**2)**(-0.5)
            else:
                tmp += (i**2 + j**2)**(-0.5)
    ML += tmp * 12.0
    return ML
    
if __name__ == '__main__':
    print Madelung_constant(400)
