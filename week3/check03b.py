"""
File: check03b.py

Purpose: Practice classes with Complex numbers.
"""

class Complex:
    """Complex number class """

    def __init__(self):
        self.real_number = 0
        self.imaginary_number = 0
    def set_real_number(self, number):
        self.real_number = number
    def get_real_number(self):
        return self.real_number
    def set_imaginary_number(self, number):
        self.imaginary_number = number
    def get_imaginary_number(self):
        return self.imaginary_number
    def prompt(self):
        self.set_real_number(input("Please enter the real part: "))
        self.set_imaginary_number(input("Please enter the imaginary part: "))
    def display(self):
        print("{} + {}i".format(self.get_real_number(),self.get_imaginary_number()))


def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    c1 = Complex()
    c2 = Complex()

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
