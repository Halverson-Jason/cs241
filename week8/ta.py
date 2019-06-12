class Time:
    def __init__(self):
        self._days = 0
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
    def get_hours(self):
        return self._hours
    def get_minutes(self):
        return self._minutes
    def get_seconds(self):
        return self._minutes
    def set_hours(self, hours):
        if hours > 23:
            self._hours = 23
        elif hours < 0:
            self._hours = 0
        else:
            self._hours = hours
    def set_minutes(self,minutes):
        if minutes > 59:
            self._minutes = 59
        elif minutes < 0:
            self._minutes = 0
        else:
            self._minutes = minutes
    def set_seconds(self,seconds):
        if seconds > 59:
            self._seconds = 59
        elif seconds < 0:
            self._seconds = 0
        else:
            self._seconds = seconds
    seconds = property(get_seconds, set_seconds)

    @property
    def minutes(self):
        return self.get_minutes()
    @minutes.setter
    def minutes(self, min):
        self.set_minutes(min)

    @property
    def hours(self):
        return self.get_hours()
    @hours.setter
    def hours(self, hour):
        self.set_hours(hour)

def main():
    time = Time()

    hour = int(input("Hours: "))
    min = int(input("Minutes: "))
    sec = int(input("Seconds: "))

    time.hour = hour
    time.minutes = min
    time.second = sec

    print(time.hour)
    print(time.minutes)
    print(time.second)

if __name__ == "__main__":
    main()