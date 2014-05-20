#Homework 2 Exercise: The Madelung constant
import math
def M(i,j,k):
    if i == 0 and j == 0 and k == 0:
        return 0
    elif (i + j + k) % 2 == 0:
            return 1.0 / math.sqrt(i**2 +j**2 + k**2)
    elif (i + j + k) % 2 == 1:
        return -1.0 / math.sqrt(i**2 + j**2 +k**2)

def M_limit(L):
    _sum = 0
    i = -L
    while i <= L:
        j = -L
        while j <= L:
            k = -L
            while k <= L:
                _sum = _sum + M(i,j,k)
                k = k + 1
            j = j + 1
        i = i + 1
    return _sum

'''
When we input L = 299 and 300, python claculated M_limit(299) and M_limit(300)
are respectiively -1.7494923084 and -1.74564329591. After averaging, we'll have
the value -1.7475678022. Approximately, it's about -1.748, so I conclude this
value to be the Madelung constant.
'''
