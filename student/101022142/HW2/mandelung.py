#2.mandelung.py
def M(i,j,k):
    if i == j == k == 0:
        return 0
    else :
        return (-1)**(i+j+k)/(i**2+j**2+k**2)**(0.5)
    

def mandelung(L):
    M_s=0
    for k in range(-L,L+1):
        for j in range(-L,L+1):
            for i in range(-L,L+1):
                M_s+=M(i,j,k)
    print M_s
    


#This is the method that we write "M" outside
#How about we just use one function rather than using two?

def mandelung_2(L):
    M_sum=0
    for k in range(-L,L+1):
        for j in range(-L,L+1):
            for i in range(-L,L+1):
                if i == j == k == 0:
                    M_cur=0
                else:
                    M_cur =(-1)**(i+j+k)/(i**2+j**2+k**2)**0.5
                    M_sum +=M_cur
    print M_sum

mandelung_2(55)
mandelung(55)
