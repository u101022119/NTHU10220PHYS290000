def factorial_rec (num):
    num = int(num)
    if num <= 1:
        return 1
    else: return factorial_rec(num-1)*num

print "0! = ",factorial_rec(0)
print "1! = ",factorial_rec(1)
print "2! = ",factorial_rec(2)
print "3! = ",factorial_rec(3)
print "4! = ",factorial_rec(4)
