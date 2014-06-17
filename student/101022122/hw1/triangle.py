
def judge_tri():
    a=input('first side of triangle:')
    b=input('second side of triangle:')
    c=input('third side of triangle:')
    d=a-b
    if d<0:
        d=-d
    if a+b>c:
        if d<c:
            print 'this can be the triangle'
        else:
            print 'this cannot be the triangle'
            return
    else:
        print 'this cannot be the triangle'
        return

judge_tri()
