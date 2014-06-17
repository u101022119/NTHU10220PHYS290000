Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
def random_list(N,a,b):
    c = []
    for i in range(N):
        c.append(random.randint(a,b))
    return c

def selection_sort(c,N):
    print random.sample(c,N)

def insertion_sort(c,N):
    for i in range(N):
        c.append(random.randint(a,b))
    print c
def bubble_sort(c):
    for i in range(len(c)):
        for j in range(len(c)-1):
            if c[j] < c[j+1]:
                temp = c[j]
                c[j] = c[j+1]
                c[j+1] = temp
    print c

a = 0
b = 100
insertion_sort(random_list(6,0,100),10)
bubble_sort(random_list(6,0,100))

class Time(object):
    def print_time(time):
        print '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second)

    def time_to_int(time):
        return time.hour*3600+time.minute*60+time.second        

    def is_after(self,other):
        return Time.time_to_int(self) > Time.time_to_int(other)

    def increment_modifier(self,second):
        a = Time.time_to_int(self)
        a = a + second
        self.hour = a/3600
        self.minute = (a%3600)/60
        self.second = (a%3600)%60
        print Time.print_time(self)

    def increment_pure(self,second):
        time3 = Time()
        a = Time.time_to_int(self)
        a = a + second
        time3.hour = a/3600
        time3.minute = (a%3600)/60
        time3.second = (a%3600)%60
        print Time.print_time(time3)

    def mul_time(self,n):
        self.hour *= n
        self.minute *= n
        self.second *= n
        a = Time.time_to_int(self)
        self.hour = a/3600
        self.minute = (a%3600)/60
        self.second = (a%3600)%60
        print Time.print_time(self)


time1 = Time()
time1.hour = 1
time1.minute = 21
time1.second = 36

time2 = Time()
time2.hour = 11
time2.minute = 20
time2.second = 1

Time.mul_time(time1,2)
