def factorial_rec(n):
    if type(n) != int or n < 0:
        return 'None'
    elif n == 0:
        return 1
    else:
        recurse = factorial_rec(n - 1)
        result = n * recurse
        return result
