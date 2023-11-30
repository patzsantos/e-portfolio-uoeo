class Time:
    """Represents the time of day."""

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

# inside class Time:

def increment(self, seconds):
    seconds += self.time_to_int()
    return int_to_time(seconds)

# inside class Time:

def is_after(self, other):
    return self.time_to_int() > other.time_to_int()

# inside class Time:

def __init__(self, hour=0, minute=0, second=0):
    self.hour = hour
    self.minute = minute
    self.second = second

# inside class Time:

def __str__(self):
    return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

# inside class Time:

def __add__(self, other):
    if isinstance(other, Time):
        return self.add_time(other)
    else:
        return self.increment(other)

def add_time(self, other):
    seconds = self.time_to_int() + other.time_to_int()
    return int_to_time(seconds)

def increment(self, seconds):
    seconds += self.time_to_int()
    return int_to_time(seconds)

# inside class Time:

def __radd__(self, other):
    return self.__add__(other)

