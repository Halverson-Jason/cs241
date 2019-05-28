
class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def prompt(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))

    def display(self):
        print("{month:02d}/{day:02d}/{year:04d}".format(month=self.month,day=self.day,year=self.year))

    def validate_month(self):
        if self.month > 0 and self.month <= 12:
            return True