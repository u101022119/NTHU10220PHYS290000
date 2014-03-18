#--------------------------exe1----------------------
def histogram(s):
    d = dict()
    for c in s:
        d[c]=1+d.get('c',0)
    return d
#-------------------------end--------------
f=histogram('fffg   ggg')
print f

def print_hist(h):
    for c in h:
        print c, h[c]
print_hist(f)
#-----keys()------------
k=dict()
k={'eo4':'fuck','fgfg':'erer'}
print "key's list : %s" %k.keys()

#-----------use keys() and sort() to build print_hist()-----------

def print_hist(histogram):
    hists = histogram.keys()
    hists.sort()
    for letter in hists:
        print letter, histogram[letter]
#--------notice : the consturture of hist was change!!
    
print_hist(f)
