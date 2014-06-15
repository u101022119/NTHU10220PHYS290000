

def judge_tri():
    a=input('first side of triangle:')
    b=input('second side of triangle:')
    c=input('third side of triangle:')
    d=a-b
    if d<0:
        d=-d
    if a+b>c:
        if d<c:
            print 'Yes'
        else:
            print 'No'
            return
    else:
        print 'No'
        return

judge_tri()
