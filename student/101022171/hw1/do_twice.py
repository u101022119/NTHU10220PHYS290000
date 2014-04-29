#File: do_twice.py
#HW1_EX3_Do_twice
#Due: 3/25/2014
#Author: 101022171

def do_twice(f, p):
    f(p)
    f(p)

def print_twice(p):
    print p
    print p

#do_twice(print_twice, 'spam')

def do_four(f, p):
    do_twice(f, p)
    do_twice(f, p)
