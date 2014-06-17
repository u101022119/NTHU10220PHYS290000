# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:54:02 2014

@author: user
"""

def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

def print_twice(s):
    print s
    print s

def modified_print_twice( f , string ):
    f(string)
    f(string)

def do_four( f , string ):
    modified_print_twice( f , string )
    modified_print_twice( f , string )

do_twice(print_spam)
print_twice('spam')
modified_print_twice(print_twice , 'spam' )
do_four(print_twice , 'spam' )