#Homework 1 exercise 10
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n ==0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n-1))

print ack(3, 4)

#when m <= 2, the function works for all n
#when m == 3, the function works for n < 8
#when m == 4, the function works for n < 1
#when m >= 5, the function doesn't work for all n
