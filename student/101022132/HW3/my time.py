class Time(object):
    def print_time(time):
        print '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second)

    def time_to_int(time):
        return time.hour*3600+time.minute*60+time.second        

    def is_after(self,other):
        return Time.time_to_int(self) > Time.time_to_int(other)

    def increment_modifier(self,second):
        y = Time.time_to_int(self)
        y = y + second
        self.hour = a/3600
        self.minute = (y%3600)/60
        self.second = (y%3600)%60
        print Time.print_time(self)

    def increment_pure(self,second):
        time3 = Time()
        y = Time.time_to_int(self)
        y = y + second
        time3.hour = y/3600
        time3.minute = (y%3600)/60
        time3.second = (y%3600)%60
        print Time.print_time(time3)

    def mul_time(self,n):
        self.hour *= n
        self.minute *= n
        self.second *= n
        y = Time.time_to_int(self)
        self.hour = y/3600
        self.minute = (y%3600)/60
        self.second = (y%3600)%60
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
