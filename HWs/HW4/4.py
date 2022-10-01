import re
class Time():
    def __init__(self, seconds = 0):
        self.sec = seconds

    def convert_to_minutes(self):
        return str(int(self.sec / 60)) + ":" + str(self.sec % 60)

    def convert_to_hours(self):
        t = self.convert_to_minutes()
        res = re.search(r'(?P<minutes>\d+):(?P<seconds>\d+)', t)
        minute = res.group("minutes")
        return str(int(int(minute) / 60)) + ":" + str(int(minute) % 60) + ":" + str(res.group("seconds"))

time = Time(3601)
print(time.convert_to_hours())  