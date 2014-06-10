class Date(object):
    """pass"""

def justfy(year):
    if year % 400 ==0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False


def increment_date(d,n):
    for i in range(n):
        if d.month==12 and d.day==31:
            d.year= d.year+1
            d.month = 1
            d.day = 1

        elif justfy(d.year) and d.month==2 and d.day==29:
            d.month = d.month +1
            d.day = 1

        elif (not justfy(d.year)) and  d.month==2 and d.day==28:
            d.month = d.month + 1
            d.day = 1

        elif d.month in ( 4, 6, 9, 11 ) and d.day==30:
            d.month = d.month +1
            d.day = 1

        elif d.day==31:
            d.month = d.month +1
            d.day = 1

        else:
            d.day= d.day+1

D = Date()
D.day =1
D.month =5
D.year =2013
increment_date(D,360)
print "%.4d/%.2d/%.2d" % (D.year,D.month,D.day)
