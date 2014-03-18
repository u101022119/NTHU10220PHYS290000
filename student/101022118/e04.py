word = 'what the fucking are you talking about'

def count(word, the):
    count = 0
    for letter in word:
        if letter == the:
            count = count +1
    print count

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter

def rright_justify(s):
    l = len(s)
    space = ' '*79
    ls = len(space)
    out = space[0:ls-l] + s
    print out

def do_twice(f):
    f()
    f()

def prin():
    print word

def do_twices(f, s):
    f(s)
    f(s)

def print_twice(s):
    print s
    print s
    
def do_four(f, s):
    do_twices(f, s)
    do_twices(f, s)


do_four(print_twice, word)
