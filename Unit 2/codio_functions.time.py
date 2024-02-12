class Time:

    def __init__(self, hour=0, minute =0, second =0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def add_time(t1, t2):
        sum_time = Time()
        sum_time.hour = t1.hour + t2.hour
        sum_time.minute = t1.minute + t2.minute
        sum_time.second = t1.second + t2.second

        if sum_time.second >= 60:
            sum_time.second -= 60
            sum_time.minute += 1

        if sum_time.minute >= 60:
            sum_time.minute -= 60
            sum_time.hour += 1

        if sum_time.hour >= 24:
            sum_time.hour -= 24

        return sum_time

    @staticmethod
    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    @staticmethod
    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

# test the code
time1 = Time(6,29,50)
time2 = Time(7,7,25)

sum_time = Time.add_time(time1, time2)

print("Sum:", sum_time.hour, ":", sum_time.minute, ":", sum_time.second)
