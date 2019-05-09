class human:
    def __init__(self):
        self.weight = 0
class Student(human):
    """ Test """
    def __init__(self):
        super().__init__()
        grade = 0
    def compile(self):
        print(self.weight)
student = Student()
student.compile()