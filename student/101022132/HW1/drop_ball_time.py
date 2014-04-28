import math

H=raw_input('H=?')
h=raw_input('h=?')
h=float(h)
H=float(H)
A=H-h
t=math.sqrt(A*2/10)
t=float(t)
T=math.sqrt(H*2/10)
T=float(T)
L=T-t
print L
