class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        if (hour <= 24 and minute <= 59 and second <= 60):
            return True

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = time_string.split(':')
        p = cls(hour, minute, second)
        return p

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
