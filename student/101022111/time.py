class Time(object):
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour,self.minute, self.second)
# inside class Time:
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
start=Time()
start.hour=1
start.minute=10
start.second=20
start.print_time()
