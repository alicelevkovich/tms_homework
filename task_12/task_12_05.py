class MyTime(object):

    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        elif isinstance(args[0], str):
            self.hours, self.minutes, self.seconds = args[0].split(' ')
        elif isinstance(args[0], MyTime):
            self.hours, self.minutes, self.seconds = args[0].hours, args[0].minutes, args[0].seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

    def __eq__(self, other):
        return (self.hours == other.hours
                & self.minutes == other.minutes
                & self.seconds == other.seconds
                )

    def __ne__(self, other):
        return (self.hours != other.hours
                & self.minutes != other.minutes
                & self.seconds != other.seconds
                )

    def __add__(self, other):
        return (self.hours + other.hours
                & self.minutes + other.minutes
                & self.seconds + other.seconds
                )

    def __sub__(self, other):
        return (self.hours - other.hours
                & self.minutes - other.minutes
                & self.seconds - other.seconds
                )

    def fill_with_zeros(self, number):
        return str(number).zfill(2)

    def __str__(self):
        hours = self.fill_with_zeros(self.hours)
        minutes = self.fill_with_zeros(self.minutes)
        seconds = self.fill_with_zeros(self.seconds)
        return f'{hours}:{minutes}:{seconds}'

    def convert_time(self):
        old_seconds = self.seconds

        self.seconds = old_seconds % 60
        self.minutes += old_seconds // 60
        old_minutes = self.minutes
        self.minutes %= 60
        self.hours += old_minutes // 60


if __name__ == '__main__':
    my_time = MyTime(22, 27, 30)
    my_time_2 = MyTime(22, 27, 45)

    wrong_time = MyTime(12, 65, 83)
    wrong_time.convert_time()

    print(my_time == my_time_2)
    print(wrong_time)
