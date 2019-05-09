class Student:
    """New class for student """
    def __init__(self):
        first_name = ""
        last_name = ""
        id = 0
    def set_first_name(self, name):
        self.first_name = name
    def get_first_name(self):
        return self.first_name
    def set_last_name(self, name):
        self.last_name = name
    def get_last_name(self):
        return self.last_name
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
def display_student(student):
    print("\nYour information:\n{} - {} {}".format(student.get_id(),student.get_first_name(),student.get_last_name()))

def prompt_student():
    student = Student()
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    id = input("Please enter your id number: ")
    student.set_first_name(first_name)
    student.set_last_name(last_name)
    student.set_id(id)
    return student

def main():
    user = prompt_student()
    display_student(user)

if __name__ == "__main__":
    main()