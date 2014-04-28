eng2sp=dict()
eng2sp={"one": "uno","two": "dogs","three": "trees"}
print eng2sp

"one" in eng2sp #true
"uno" in eng2sp #false

vals=eng2sp.values()
"uno" in vals   #true

def histogram(s):  #set s= some str ­p¼Æ
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c] +=1
    return d
