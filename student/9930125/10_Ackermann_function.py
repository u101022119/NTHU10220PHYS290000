import math
m, n = int(raw_input('ENTER THE VALUE OF THE M: ')), int(raw_input('ENTER THE VALUE OF THE N: '))
def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0:
        if n == 0:
            return ack(m-1, 1)
        if n > 0:
            return ack(m-1, ack(m, n-1))

print ack(m, n)
