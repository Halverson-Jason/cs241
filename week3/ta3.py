class RationalNumber:
    _numerator=None
    _denominator=None
    def __init__(self):
        self.set_numerator(0.0)
        self.set_denominator(1.0)
    def display(self):
        print("{}/{}".format(int(self._numerator),int(self._denominator)))
    def set_numerator(self, numerator):
        self._numerator = numerator
    def set_denominator(self, denominator):
        self._denominator = denominator
    def prompt(self):
        self.set_numerator(float(input("Enter the numerator: ")))
        self.set_denominator(float(input("Enter the denominator: ")))
    def display_decimal(self):
        print(self._numerator / self._denominator)

def main():
    rational_number = RationalNumber()
    rational_number.prompt()
    rational_number.display()
    rational_number.display_decimal()

if __name__ == "__main__":
    main()