"""
#File:   catalan.py
#Title:  Catalan numbers
#Due:    4/22/2014
#Author: 101022171, chin-hua Cheng
"""
def catalan(): 
      
    a = 1
    i = 0.0
    print "n Cn"
    while 1: 
        b = a*((4*i + 2.0)/(i + 2))
        if a<1000000000:
            print int(i),"",int(a)
            a = b
            i+=1
        else :
            print int(i),"",int(a), "which is over one billion."
            break
          
catalan()