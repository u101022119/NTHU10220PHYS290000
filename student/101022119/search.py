word='correct'
def find(word, letter):
    index=0
    while index < len(word):
        if word[index] == letter:
            print 'a'
            return index
            print 'b'
        index = index + 1
    print "c"
    return -1
    
find(word, 'p')
