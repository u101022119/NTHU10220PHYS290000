##from __future__ import division
limit = input('Prints in increasing order all Catalan numbers less than or equal to')

catalan = 1

n = 0.0
print 'C_ 0 = 1'

while ((4*n + 2)/(n + 2))*catalan <= limit :

    catalan = ((4*n + 2)/(n + 2))*catalan
    n = n + 1
    print 'C_',n,'=',catalan
