#1-4.do_twice.py
#In fact,I don't understand what this following saying about ?
'''
Modify do_twice so that it takes two arguments, a
function object and a value, and calls the function twice,
passing the value as an argument.
'''
def print_twice(string):
    print string
    print string

string='fun you'
print_twice(string)

def print_one(string):
    print string

def do_twice(f,x):
    f(x)
    f(x)

def do_four(do_twice,f,x):
    do_twice(f,x)
    do_twice(f,x)

s='like'
do_four(do_twice,print_one,s)
