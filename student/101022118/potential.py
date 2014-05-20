# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:59:20 2014

@author: user
"""

def U1(i,j,k):
    s = i**2 + j**2 + k**2
    U = s ** ( -0.5 )
    u = U * ( -1 ) ** ( i + j + k )
    return u

def U( i , j , k ):
    if i == 0 & j == 0 & k == 0:
        return 0
    else:
        return U1( i , j , k )

def R(l):
    r = range(0 , l * 2 + 1 )
    return r

def Uz( x , y , l ):
    z = 0
    for k in R(l):
        z += U( x , y , k - l )
    return z

def Uy( x , l ):
    y = 0
    for j in R(l):
        y += Uz( x , j - l , l )
    return y

def Ux( l ):
    x = 0
    for i in R(l):
        x += Uy( i - l , l )
    return x
    
def u():
    l = int(raw_input("Order of crystal:" ))
    print Ux(l)

u()
