class GPA:
    def __init__(self):
        self._gpa_value = 0.0
    def _get_gpa(self):
        return self._gpa_value
    def _set_gpa(self, value):
        self._gpa_value = value
    def _get_letter(self):
        if self._get_gpa() < 4.0:
            if self._get_gpa() < 3.0:
                if self._get_gpa() < 2.0:
                    if self._get_gpa() < 1.0:
                        return 'F'
                    return 'D'
                return 'C'
            return 'B'
        return 'A'
    def _set_letter(self, letter):
        if letter == 'A':
            self._set_gpa(4.0)
        elif letter == 'B':
            self._set_gpa(3.0)
        elif letter =='C':
            self._set_gpa(2.0)
        elif letter =='D':
            self._set_gpa(1.0)
        elif letter =='F':
            self._set_gpa(0.0)
    gpa = property(_get_gpa, _set_gpa)
    @property
    def letter(self):
        return self._get_letter()
    @letter.setter
    def letter(self,letter):
        self._set_letter(letter)

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()