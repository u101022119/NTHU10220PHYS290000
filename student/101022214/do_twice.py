##def do_twice(f):
##    f()
##    f()
##    return
##
##def print_spam():
##    print "spam"
##    return

def myprint (mystr):
    print mystr
    return

def do_twice(fun,val):
    fun(val)
    fun(val)
    return

def print_twice(mystr):
    print mystr
    print mystr
    return
print 'print_twice(spam) = '
print_twice('spam')

def do_four(fun,val):
    do_twice(fun,val)
    do_twice(fun,val)
    return
print 'do_four(myprint,spam) = '
do_four(myprint,'spam')
