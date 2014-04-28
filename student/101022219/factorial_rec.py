n = float (raw_input('Enter the value of n:'))
def factorial_rec(n):
    if n == 0:
        return 1
    elif n == int(n):
        recurse = factorial_rec(n-1)
        result = n * recurse
        return result    
print factorial_rec(n)
