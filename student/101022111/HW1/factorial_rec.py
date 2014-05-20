n=int(raw_input('What is your n:'))
def factorial_rec (num):
    num = int(num)
    if num <= 1:
        return 1
    else: return factorial_rec(num-1)*num
print n,'!=',factorial_rec(n)
