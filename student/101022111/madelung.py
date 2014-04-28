M=int(raw_input('What is your L : '))

def madelung(L):
    i=-L
    j=-L
    k=-L
    p=0
    while i<L:
        while j<L:
            while k<L:
                if k==0:
                    k=k+1
                    return k
                else:
                    n=(i*i+j*j+k*k)**0.5
                    p=n+p
                    k=k+1
                    return p,k
            j=j+1
            k=-L
            if j==0:
                j=j+1
                return j
            else:
                while k<L:
                    if k==0:
                        k=k+1
                        return k
                    else:
                        n=(i*i+j*j+k*k)**0.5
                        p=n+p
                        k=k+1
                        return p,k
                return p,j
        i=i+1
        j=-L
        if i==0:
            i=i+1
            return i
        else:
            while j<L:
                while k<L:
                    if k==0:
                        k=k+1
                        return k
                    else:
                        n=(i*i+j*j+k*k)**0.5
                        p=n+p
                        k=k+1
                        return p,k
                j=j+1
                k=-L
                if j==0:
                    j=j+1
                    return j
                else:
                    while k<L:
                        if k==0:
                            k=k+1
                            return k
                        else:
                            n=(i*i+j*j+k*k)**0.5
                            p=n+p
                            k=k+1
                            return p,k
                return p,j
        return p,i
    print p
madelung(M)
