'''
def do_twice(f):
    f()
    f()

def print_spam():
    print'spam'

do_twice(print_spam)
'''
'''
def do_twice(f,v):
    f(v)
    f(v)

def print_spam(spam):
    print spam

do_twice(print_spam,'Helen')
'''
'''
def print_twice(spam):
    print'spam'
    print'spam'

def do_twice(f,v):
    f(v)
    f(v)

do_twice(print_twice,'spam')
'''
'''
def print_one(spam):
    print'spam'
    
def do_twice(f,v):
    f(v)
    f(v)

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

do_four(print_one,'spam')
'''

