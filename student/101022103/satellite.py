T= float(raw_input('Enter period(sec):'))

def sate(T):
    h= ((6.67*10**(-11))*(5.97*10**2)*T/4/(3.14**2))**(1/3)-6417
    if h>=0:
        print h
    else:
        print 'invalid input'

sate(T)

