from math import *
import pygame as pyg

sp={0:' ',1 : 'o',-1 : 'x'}
direct = {(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)}
    
def DisplayTable(A):
    for i in range(9):
        if i == 0:
            print '0 1 2 3 4 5 6 7 8'
        else:
            ser = [sp[A[i,j+1]] for j in range(8)]
            a=' '
            print str(i)+' '+ a.join(ser)
    print ''
    print ''
    return 0

def Initialize():
    A={(i+1,j+1): 0 for i in range(8) for j in range(8)}
    A[4,4]=1
    A[5,5]=1
    A[4,5]=-1
    A[5,4]=-1
    return A

A=Initialize()
DisplayTable(A)

def InTable(x,y):
    if x in range(1,9) and y in range(1,9):
        return 0
    return 1

def EatLineTest(t,x,y,a,b):
    tempx,tempy=x+a,y+b
    if InTable(tempx,tempy) == 1:
        return 1
    if A[tempx,tempy] == t:
        return 1
    while(True):
        if InTable(tempx,tempy) == 1:
            return 1
        if A[tempx,tempy] == t:
            break
        tempx+=a
        tempy+=b
    return 0

def InputTest(t,x,y):
    test=1
    if A[x,y] != 0:
        return 1
    for a,b in direct:
        msg=EatLineTest(t,x,y,a,b)
        test*=msg
    return test


def EatLine(t,x,y,a,b):
    if EatLineTest(t,x,y,a,b) == 1:
        return 'fail'
    tempx,tempy=x+a,y+b
    while(True):
        if A[tempx,tempy] == -t:
            A[tempx,tempy] = t
        elif A[tempx,tempy] == t:
            break
        tempx+=a
        tempy+=b
    A[x,y] = t
    return 'succive'

def Eat(t,x,y):
    if A[x,y] != 0:
        return 1
    for a,b in direct:
        EatLine(t,x,y,a,b)
    return 0

def Input(t):
    t=(-1)**t
    correct = 1
    while(correct != 0):
        x,y = input('please enter x & y : ')
        correct = InputTest(t,x,y)
        print ''
    Eat(t,x,y)
    DisplayTable(A)
    return

t=0
while(True):
    Input(t)
    t+=1
    

            
