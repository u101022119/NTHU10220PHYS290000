def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)

def modified_do_twice(function, value):
    function(value)
    function(value)

def print_twice(string):
    print string
    print string

modified_do_twice(print_twice, 'spam')

def do_four(function, value):
    modified_do_twice(function, value)
    modified_do_twice(function, value)


    
